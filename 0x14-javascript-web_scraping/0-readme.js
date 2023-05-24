#!/usr/bin/node

const fs = require("fs");
const file_name = process.argv[2];


fs.readFile(file_name, "utf-8", (err, content) => {
	if (err) {
	  console.log(err)
	} else {
	  console.log(content);
	}
});
