#!/usr/bin/node
const arg = process.argv;
const elmtOneInArr = arg.includes(arg[2]);
const elmtTwoInArr = arg.includes(arg[3]);

if (elmtOneInArr === true && elmtTwoInArr === true) {
  console.log(`${arg[2]} is ${arg[3]}`);
} else if (elmtOneInArr === true && elmtTwoInArr === false) {
  console.log(`${arg[2]} is ${arg[3]}`);
} else if (elmtOneInArr === false && elmtTwoInArr === false) {
  console.log(`${arg[2]} is ${arg[3]}`);
}
