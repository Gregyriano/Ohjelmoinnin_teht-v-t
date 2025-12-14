'use strict'

const numbers = [];

let number;

while(number !== 0){
    number = parseInt(prompt("Kirjoita numero ja 0 jos haluat lopeta."));
    numbers.push(number);
}
numbers.sort((a,b) => b-a);
for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}