'use strict'

const num_1 = parseInt(prompt('Give me first number, pls'));
const num_2 = parseInt(prompt('Give me second number, pls'));
const num_3 = parseInt(prompt('Give me third nember, pls'));

const sum = num_1 + num_3 + num_2;
const  product = num_2 * num_1 * num_3;
const average = (num_3 + num_2 + num_1);

document.querySelector('.output').textContent = `Sum is ${sum}, product is ${product}, average is ${average}`;

