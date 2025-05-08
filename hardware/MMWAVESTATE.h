// mmwave.h
#include "Arduino.h"
#include <PicoSoftwareSerial.h>
#include <humanstaticLite.h>
#include <WiFiNINA.h>

#define OFF 0
#define STANDBY 1
#define DARK 2
#define DIM 3
#define LIGHT 4
#define BRIGHT 5 
#define BOOT 6 

const uint8_t ON_PIN   = 11;    // Drives Zero2Go “SW” / Pi GPIO4

const int TX_PIN = 5;           // Transmit Pin
const int RX_PIN = 6;           // Receive Pin

// Message Settigs
const unsigned char open_buff[10] = {0x53, 0x59, 0x08, 0x00, 0x00, 0x01, 0x01, 0xB6, 0x54, 0x43};
const unsigned char close_buff[10] = {0x53, 0x59, 0x08, 0x00, 0x00, 0x01, 0x00, 0xB5, 0x54, 0x43};

// Proxmity inquiry
const unsigned char proximity_inquiry[10] = {0x53, 0x59, 0x80, 0x8B, 0x00, 0x01, 0x0F, 0xC7, 0x54, 0x43};

// Different room properties
const unsigned char set_office_scene[10] = {0x53, 0x59, 0x05, 0x07, 0x00, 0x01, 0x02, 0xB7, 0x54, 0x43};
const unsigned char set_bedroom_scene[10] = {0x53, 0x59, 0x05, 0x07, 0x00, 0x01, 0x01, 0xB6, 0x54, 0x43};

// Customised tick resolution(s) (1 TICK = 500 MS DEFAULT)
// 500 MS timings prevents 
constexpr uint16_t  TICK_MS             = 500;             
constexpr uint16_t  COUNT_10S           = 20;              
constexpr uint16_t  COUNT_BOOT_50S      = 100;
constexpr uint32_t  S_COUNT_5MIN        = 5ul * 60 * 10;   
constexpr uint32_t  O_COUNT_1HOUR       = 60ul * 60 * 10;  
constexpr uint16_t  OFF_300MS           = 3; 
// Bounce tick resolution for button press
const uint16_t      PRESS_MS            = 200; 