#!/usr/bin/node
const arg = process.argv;
const num = isNaN(parseInt(arg[2])) ? 'Missing number of occurrences' : parseInt(arg[2]);
if (typeof (num) !== 'number') {
  console.log(num);
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
