'use strict';

const express = require('express');
var path = require('path');

const port = 8080;
const host = '0.0.0.0';

const app = express();

app.use(express.static(path.resolve('public')));


app.listen(port, host, () => {
	console.log(`Serving running on localhost:${port}`);
});