'use strict'




const koirat = [];
const number = prompt('KIrjoitan kuinka monta nimea haluat listassa: ');

for (let i = 0; i < number; i++ ){
    let nimi = prompt('Kirjoita nimi: ');
    koirat.push(nimi);
}
koirat.sort();
koirat.reverse();
console.log(koirat);

const el = document.getElementById('koirat');
const ul = document.createElement('ul');
el.appendChild(ul);

for (let i = 0; i < koirat.length; i++) {
  let li = document.createElement('li');
  li.appendChild(document.createTextNode(koirat[i]));
  ul.appendChild(li);
}
