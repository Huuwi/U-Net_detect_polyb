const path = require("path")


const getHomePage = (req, res) => {
    res.sendFile(path.resolve("./public/home_page.html"))
}
const sendImage = (req, res) => {
    res.send(req.body)
    console.log(req.body);
}


module.exports = {
    getHomePage: getHomePage,
    sendImage: sendImage,
}