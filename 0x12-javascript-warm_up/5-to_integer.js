#!/usr/bin/node
const arg = process.argv;
const arrLen = arg.length;
const elmtInArr = arg.includes(arg[2]);
switch (true) {
  case arrLen < 3:
    console.log('Not a number');
    break;
  case elmtInArr === true:
    console.log(`${isNaN(parseInt(arg[2])) ? 'Not a number' : 'My number: ' + parseInt(arg[2])}`);
    break;
}
