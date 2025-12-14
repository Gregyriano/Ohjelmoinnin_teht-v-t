'use strict'

const numbers = [];

do {
    let number = parseInt(prompt("Kirjoita numero: "));
    if (numbers.includes(number)){
        break;
    }
    numbers.push(number);

} while (true)

numbers.sort((a,b) => a-b);

for (let i = 0; i < numbers.length; i++){
    console.log(numbers[i]);
}

