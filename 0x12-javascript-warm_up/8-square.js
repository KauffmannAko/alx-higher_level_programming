#!/usr/bin/node
const arg = process.argv;
const num = isNaN(parseInt(arg[2])) ? 'Missing size' : parseInt(arg[2]);
if (typeof (num) !== 'number') {
  console.log(num);
} else {
  for (let l = 0; l < num; l++) {
    let temp = '';
    for (let i = 0; i < num; i++) {
      temp = temp + '' + 'X';
    }
    console.log(temp);
  }
}
