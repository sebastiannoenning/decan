const express = require('express')
const cors = require('cors')
const mysql = require('mysql')
const bodyParser = require('body-parser')
const router = require('./routes/router')
const db = require('./configs/db')

const app = express()

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended:false}))

db.connect((err) => {
  if (err){
    console.log(err)
  }
  console.log('Database Connected')
});

const corsOptions = {
  origin:'*',
  credentials: true,
  optionSuccessStatus: 200
}

app.use(cors(corsOptions))
app.use('/', router)

const port = 3000
const server = app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
})

