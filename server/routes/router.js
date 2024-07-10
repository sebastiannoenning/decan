//export{}
const express = require('express')
const db = require('./config/db.js')
const router = express.Router()

router.get('/users', (req,res) => {
    const sql = 'SELECT * FROM Users';
    db.query(sql, (err, data) => {
        if (err) return res.json(err);
        return res.json(data);
    }) 
})

module.exports = router;
