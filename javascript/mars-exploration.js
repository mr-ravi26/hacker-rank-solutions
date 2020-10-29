'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the marsExploration function below.
function marsExploration(s) {

    var n = s.length;
    var r = "SOS".repeat(n / 3);
    var t = 0;


    for (var i = 0; i < n; i++) {
        if (s[i] !== r[i]) {
            t++;
        }
    }

    return t;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const s = readLine();

    let result = marsExploration(s);

    ws.write(result + "\n");

    ws.end();
}
