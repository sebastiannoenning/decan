
#include "MMWAVESTATE.h"
// STATE COUNTERS
uint16_t  count         = 0;          // 10 seconds~ -> Open to potential user-editing in a future implementation
uint32_t  s_count       = 0;          // 5 minutes
uint32_t  o_count       = 0;          // 1 hour

// State Variable
int   proxState    = OFF;

// PicoSoftSerial
SoftwareSerial SoftSerial1(RX_PIN, TX_PIN);

// Radar
HumanStaticLite radar = HumanStaticLite(&Serial1);

// PROXIMITY PARSE FUNC
float proximityParser()
{
  float ds = radar.dis_static;
  float dm = radar.dis_move;
  if (ds == 0.0f) ds = 6.0f;       // If <1, convert to 6m
  if (dm == 0.0f) dm = 6.0f;
  return (ds < dm) ? ds : dm;      // Return cleaned value 
}

void togglePower() {
  // Momentarily pull line LOW, then let it float high again
  pinMode(ON_PIN, OUTPUT);
  digitalWrite(ON_PIN, LOW);
  delay(PRESS_MS);
  pinMode(ON_PIN, INPUT);     // high‑impedance → Pi’s pull‑up restores HIGH
}

// Convert integer to byte value
byte int2Brightness(int number) {
  if      (number > 100) { number = 100 ; } // Restrict upper bound to 100
  else if (number < 0)   { number = 0 ; }   // Restrict lower bound to 0
  number = (((100 - number)*255)/100) ;     // Flip the number | 0 is Max brightness and 255 is Minimum
  return (byte)(number);
}

void presenceTask()
{
  if (count    ) --count;
  if (s_count  ) --s_count;        // Only triggered on DARK
  if (o_count  ) --o_count;        // Only triggered on STANDBY

  const float prox = proximityParser(); // Current Proximity (m)

  switch (proxState) {

    // OFF, IF MOVEMENT TURN ON PI AND SWAP TO BOOT
    case OFF:
      if (prox < 6.0f) {
        analogWrite(LEDR, int2Brightness(100)) ;              // Turn LED Red to 50 Brightness
        analogWrite(LEDG, int2Brightness(20)) ;               // Turn LED Green to 50 Brightness
        togglePower();                                   // power the Pi
        proxState = BOOT;  count = COUNT_BOOT_50S;
        Serial.println("BOOT");
      }
      break;

    // BOOT, INTERMEDIATE STATE WHILE PI TURNS ON. BRIGHTNESS ENABLED AFTER
    case BOOT:
      if (count == 0) {                           // 50 s --> Run main
        analogWrite(LEDR, int2Brightness(0)) ;                // Turn LED Red to 0 Brightness
        analogWrite(LEDG, int2Brightness(100)) ;              // Turn LED Green to 100 Brightness
        proxState = BRIGHT;  count = COUNT_10S;
        Serial.println("BRIGHT");
      }
      break;
    // BRIGHT, TRIGGERED ON SUB<2M RANGE
    case BRIGHT:
      if (count == 0 && prox >= 2.0f) {     
        analogWrite(LEDR, int2Brightness(80)) ;                // Turn LED Red to 80 Brightness
        analogWrite(LEDG, int2Brightness(80)) ;               // Turn LED Green to 80 Brightness                   
        proxState = LIGHT;  count = COUNT_10S;
        Serial.println("LIGHT");
      } else if (count == 0) {                   
        count = COUNT_10S;
      }
      break;
    // LIGHT, TRIGGERED ON 2<P<3M RANGE
    case LIGHT:
      if (count == 0 && prox < 2.0f) {
        analogWrite(LEDR, int2Brightness(0)) ;                // Turn LED Red to 0 Brightness
        analogWrite(LEDG, int2Brightness(100)) ;              // Turn LED Green to 100 Brightness
        proxState = BRIGHT;  count = COUNT_10S;
        Serial.println("BRIGHT");
      }
      else if (count == 0 && prox > 3.0f) {
        analogWrite(LEDR, int2Brightness(100)) ;                // Turn LED Red to 100 Brightness
        analogWrite(LEDG, int2Brightness(65)) ;               // Turn LED Green to 65 Brightness
        proxState = DIM;     count = COUNT_10S;
        Serial.println("DIM");
      }
      else if (count == 0) {                     
        count = COUNT_10S;
      }
      break;
    // DIM, TRIGGERED ON 4<P<5M RANGE
    case DIM:
      if (count == 0 && prox < 3.0f) {
        analogWrite(LEDR, int2Brightness(80)) ;                // Turn LED Red to 80 Brightness
        analogWrite(LEDG, int2Brightness(80)) ;               // Turn LED Green to 80 Brightness
        proxState = LIGHT;  count = COUNT_10S;
        Serial.println("LIGHT");
      }
      else if (count == 0 && prox > 4.0f) {
        analogWrite(LEDR, int2Brightness(100)) ;              // Turn LED Red to 100 Brightness
        analogWrite(LEDG, int2Brightness(20)) ;               // Turn LED Green to 20 Brightness
        proxState = DARK;    count = COUNT_10S;
        s_count = S_COUNT_5MIN;                 
        Serial.println("DARK");
      }
      else if (count == 0) {                      
        count = COUNT_10S;
      }
      break;
    // DARK, TRIGGERED ON 5< RANGE
    case DARK:
      //
      if (count == 0 && prox < 4.0f) {
        analogWrite(LEDR, int2Brightness(100)) ;                // Turn LED Red to 100 Brightness
        analogWrite(LEDG, int2Brightness(65)) ;               // Turn LED Green to 65 Brightness
        proxState = DIM;     count = COUNT_10S;
        Serial.println("DIM");
        break;
      }
      if (count == 0) count = COUNT_10S;
      if (s_count == 0 && prox > 5.0f) {
        analogWrite(LEDR, int2Brightness(100)) ;              // Turn LED Red to 100 Brightness
        analogWrite(LEDG, int2Brightness(0)) ;                // Turn LED Green to 0 Brightness
        proxState = STANDBY;  o_count = O_COUNT_1HOUR;  count = COUNT_10S;
        Serial.println("STANDBY");
      }
      break;
    // STANDBY
    case STANDBY:
      if (count == 0 && prox < 5.0f) {
        analogWrite(LEDR, int2Brightness(100)) ;              // Turn LED Red to 100 Brightness
        analogWrite(LEDG, int2Brightness(20)) ;               // Turn LED Green to 20 Brightness
        proxState = DARK;     s_count = S_COUNT_5MIN;  count = COUNT_10S;
        Serial.println("DARK");
        break;
      }
      if (o_count == 0) {
        analogWrite(LEDR, int2Brightness(0)) ;              // Turn LED Red to 0 Brightness
        analogWrite(LEDG, int2Brightness(0)) ;               // Turn LED Green to 0 Brightness
        proxState = OFF;      count = OFF_300MS;
        togglePower();                             
        Serial.println("OFF");
      }
      else if (count == 0)  count = COUNT_10S;
      break;
  }
}

/* ───────────────────────────  MAIN LOOP  ─────────────────────────── */

void setup()
{
  pinMode(ON_PIN, INPUT); 

  analogWrite(LEDR, int2Brightness(0)) ;              // Turn LED Red to 100 Brightness
  analogWrite(LEDG, int2Brightness(0)) ;               // Turn LED Green to 50 Brightness

  Serial.begin(115200);
  Serial1.begin(115200);
  delay(1000);

  while(!Serial);

  radar.checkSetMode_func(open_buff, 10, false);
  delay(1000);

  Serial.println("Ready");
}

void loop()
{
  static unsigned long lastTick = 0;
  if (millis() - lastTick >= TICK_MS) {             // 100‑ms scheduler
    lastTick += TICK_MS;

    radar.recvRadarBytes();                      // get radar frames
    radar.HumanStatic_func(false);
    Serial.print("Distance ");
    Serial.print(radar.dis_static);
    Serial.print(" : ");
    Serial.println(radar.dis_move);
    presenceTask();                             // run the task
  }
}
