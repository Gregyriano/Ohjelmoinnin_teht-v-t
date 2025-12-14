'use strict'




const nimet = [];
const number = prompt('KIrjoitan kuinka monta nimea haluat listassa: ');

for (let i = 0; i < number; i++ ){
    let nimi = prompt('Kirjoita nimi: ');
    nimet.push(nimi);
}
nimet.sort();
console.log(nimet);

const el = document.getElementById('nimet');
const ol = document.createElement('ol');
el.appendChild(ol);


for (let i = 0; i < nimet.length; i++){
     let f = document.createElement('li');
     f.appendChild(document.createTextNode(nimet[i]));
     ol.appendChild(f);
}