//export{}
const express = require('express')
const db = require('../configs/db');
const router = express.Router()

router.get('/users', (req,res) => {
    const sql = 'SELECT * FROM Users';
    db.query(sql, (err, data) => {
        if (err) return res.json(err);
        return res.json(data);
    }) 
})

router.get('/events', (req,res) => {
    const sql = 'SELECT * FROM Events';
    db.query(sql, (err, data) => {
        if (err) return res.json(err);
        return res.json(data);
    }) 
})

router.get('/user/events', (req,res) => {
    const { username } = req.body;

    const sql = 'SELECT * FROM Events WHERE (SELECT UserID FROM Users WHERE Username = ?)';
    db.query(sql, [username], (err, data) => {
        if (err) return res.json(err);
        if (data.length > 0){ return res.json({data, message: 'success'})
        } else { return res.json({auth: false, message: 'incorrect username or password'}); }
    }) 
})

router.post('/login', (req,res) => {
    const { username , password } = req.body;

    const sql = 'SELECT * FROM Users WHERE Username = ? AND Password = ?';
    db.query(sql, [username, password], (err, data) => {
        if (err) return res.json(err);
        if (data.length > 0){ return res.json({auth: true, message: 'success'})
        } else { return res.json({auth: false, message: 'incorrect username or password'}); }
    }) 
})

module.exports = router;
