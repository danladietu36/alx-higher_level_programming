#!/usr/bin/node

const fs = require("fs")
const file_path = process.argv[2]
const data = process.argv[3]

fs.writeFile(file_path, "utf_8", data, (err) => {
	// throw error incase of error
	if (err) throw err;
});
