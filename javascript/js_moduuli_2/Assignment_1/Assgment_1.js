'use strict'

let  numbers = [];

for (let i = 1; i < 6; i++){
    let puk = prompt(`Give me a ${i} number`);
    numbers.push(puk);
}

console.log(numbers);

for (let i = 4; i >= 0; i--){
    console.log(numbers[i]);
}

