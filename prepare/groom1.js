// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

const findCount = (input) => {
	let str = input[0]
	let count1 = str.match(/1/g)?.length;
	let count2 = str.match(/I/g)?.length;
	let count3 = str.match(/l/g)?.length;
	let count4 = str.match(/\|/g)?.length;
	
	return `${count1}\n${count2}\n${count3}\n${count4}`
}

const input = [];
rl.on("line", function(line) {
	input.push(line)
	rl.close();
}).on("close", function() {
	console.log(findCount(input));
	process.exit();
});
