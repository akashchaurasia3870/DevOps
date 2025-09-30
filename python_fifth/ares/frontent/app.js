var express = require('express');
var app = express();
var path = require('path');
app.use(express.static(path.join(__dirname, 'public')));
app.set('view engine', 'ejs');

const URL = process.env.BACKEND_URL || "http://localhost:5000/api";
const fetch = (...args) =>
    import('node-fetch').then(({ default: fetch }) => fetch(...args));

app.get('/', async function (req, res) {
    try {
        let response = await fetch(URL, { method: "GET" });
        let json = await response.json();

        console.log("response:", json);
        // json looks like { data: ... }
        res.render('index', { data: json.data });
    } catch (err) {
        console.error(err);
        res.status(500).json({ msg: 'Internal Server Error.' });
    }
});

app.listen(3000, function () {
    console.log('Ares listening on port 3000');
});
