const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "public")));

app.post("/submit", async (req, res) => {
  try {
    const response = await axios.post("http://backend:5000/api", req.body);
    res.send(`
      <h2>Response from Backend</h2>
      <p>${response.data.message}</p>
      <a href="/form.html">Go Back</a>
    `);
  } catch (error) {
    res.status(500).send("Error communicating with backend");
  }
});

app.listen(3000, () => {
  console.log("Frontend running on port 3000");
});
