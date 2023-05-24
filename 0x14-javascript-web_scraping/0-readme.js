#!/usr/bin/node

const first_arg = require("fs");
const file_name = process.argv[2];


first_arg.readFile(filename, "utf-8", (error, content) =>
	if (error) {
		console.log(error)
	}
	else {
		console.log(context);
	}
});
