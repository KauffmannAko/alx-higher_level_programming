#!/usr/bin/node
const arg = process.argv;
const argLen = arg.length;
if (argLen < 3) {
  console.log('No argument');
} else if (argLen === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
