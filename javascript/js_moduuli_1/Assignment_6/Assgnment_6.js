'use strict'

const answer = confirm('Should I calculate the square root');

if (answer === true) {
   let sqrt = parseFloat(prompt('Give me a number: '));
   while (sqrt <= 0) {
      sqrt = parseFloat(prompt('The number must be positive. Re-enter the number.'));
   }
   const sqrt1 = Math.sqrt(sqrt)
   document.querySelector('.output').textContent = `Here is your number: ${sqrt1}`;
}
