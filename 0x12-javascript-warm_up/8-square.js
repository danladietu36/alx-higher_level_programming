#!/usr/bin/node
const x = process.argv[2];

if (!parseInt) {
	console.log('Missing size');
} else {
	for(let i = 0; i < x; i++) {
	let y = 0;
	let myVar = '';

	while (y < myVar) {
		myVar = myVar + 'X';
		y++;
	}
	console.log(myVar);
	}
}
