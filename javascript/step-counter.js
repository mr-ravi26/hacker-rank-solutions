'use strict';

const fs = require('fs');
const assert = require('assert');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
  inputString += inputStdin;
});

process.stdin.on('end', function() {
  inputString = inputString.split('\n');

  main();
});

function readLine() {
  return inputString[currentLine++];
}

const counter = (function counter() {
  let value = 0;
  return {
    getValue: function() {
      return value;
    },
    changeBy: function(k) {
      value += k;
    },
  }
})();
function getFixedCounter(k) {
    
    let myCounter = counter;
    return {
        increment: () => {
            myCounter.changeBy(k);
        },
        decrement: () => {
            myCounter.changeBy(-k);
        },
        getValue: () => {
            return myCounter.getValue();
        }
    }
}
function main() {