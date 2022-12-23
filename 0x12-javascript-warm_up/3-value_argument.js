#!/usr/bin/node
const arg = process.argv;
const elmtInArr = arg.includes(arg[2]);
if (elmtInArr === false) {
  console.log('No argument');
} else { console.log(arg[2]); }
