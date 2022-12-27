#!/usr/bin/node
const arg = process.argv;
const arrLen = arg.length;
if (arrLen === 2 || arrLen === 3) {
  console.log(0);
} else {
  const newArg = arg.map(function (x) {
    return parseInt(x, 10);
  });
  function isInt (x) {
    if (!isNaN(x)) {
      return x;
    }
  }
  const finalArg = newArg.filter(isInt);
  const max = Math.max.apply(null, finalArg);
  finalArg.splice(finalArg.indexOf(max), 1);
  const secMax = Math.max.apply(null, finalArg);
  console.log(secMax);
}
