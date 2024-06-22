const express = require('express');
const server = express();
const multer = require('multer');
const base64 = require('base64-stream');
const axios = require('axios');

server.listen(8181, function(){
	console.log('started the server...');
});

server.get('/home', function(req, res){
	console.log('home page sent');
	res.sendFile(__dirname+'/homePage.html');
});

const upload = multer({
	storage : multer.memoryStorage()
});

server.post('/convert', upload.single('file'), async (req, res) => {
	console.log('converting audio to base64 string');
    const audio = req.file.buffer;    
    const baseString = audio.toString('base64');
    console.log('sending data to python server');
	
	try {
	    const response = await axios.post('http://127.0.0.1:5000/convert', {
	        audio: baseString
	    });
	    console.log(response.data);
	    res.send(response.data);
	} catch (error) {
	    console.error(error);
	}
});
