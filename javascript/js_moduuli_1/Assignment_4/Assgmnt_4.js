'use strict'


const result =  Math.ceil(Math.random()*4);
console.log(result);

const name = prompt('Give me your name: ')
let Class;
switch (result) {
    case 2:
        Class = "Ravenclaw";
        break;
    case 3:
        Class = "Slytherin";
        break;
    case 4:
        Class = "Hufflepuff";
        break;
    default:
        Class = "Gryffindor";
}


document.querySelector('.output').textContent = `${name}, you are ${Class}`;