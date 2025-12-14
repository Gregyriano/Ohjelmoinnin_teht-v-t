'use strict'

let year = parseInt(prompt('Write a year: '));

if (year % 4 == 0 || year % 100 == 0 &&  year % 400 == 0){
    document.querySelector('.output').textContent = 'This year is a leap year.';
}
else {
    document.querySelector('.output').textContent = 'This year is not a leap year';
}