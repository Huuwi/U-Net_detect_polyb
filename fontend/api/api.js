const api = require("express").Router()
const controller = require("../controller/controller.js")

api.get("/", (req, res) => { controller.getHomePage(req, res) })
api.post("/image_from_FE", (req, res) => { controller.sendImage(req, res) })

module.exports = api