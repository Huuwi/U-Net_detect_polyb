const express = require("express")
const path = require("path")
const fs = require("fs")
const bodyParser = require("body-parser")
const api = require("./api/api.js")


const app = express()

app.use(express.static(__dirname + "/public"))
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))

app.use(api)








app.listen(6969, () => { console.log("server fontend running on port 6969"); })
