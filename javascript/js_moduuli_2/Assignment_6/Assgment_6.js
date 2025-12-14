'use strict'


function dice() {
  return Math.ceil(Math.random()*6);
}

    const el = document.getElementById('numbers');
    const ul = document.createElement('ul');
    el.appendChild(ul);

 let numero;
do{
    numero = dice();
    let li = document.createElement('li');
    li.appendChild(document.createTextNode(numero));
    ul.appendChild(li);
} while(numero !== 6)