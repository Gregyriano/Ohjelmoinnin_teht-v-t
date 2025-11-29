console.log("moro");


let emptyArray = [];

//taulukko array
let items = [1, 2, 3, {name : 'Konsta'}, [0,1,2], 'merkkijono'];
console.log(items);



console.log(items[3]);               // Alkioon viitataan indeksillä

items[0] = 99;                       // Alkion arvoa voidaan muuttaa indeksin avulla
console.log(items);

items[9] = 'Olen uusi alkio';
console.log(items);

console.log(items[6]);     //välissä on nyt määrittelemätön alkio "undefined". Ei tartte vielä tästä olla huolissaan.

let fruits = ['Banaani', 'Mango', 'Pear', 'Strawberry'];
console.log(fruits);
console.log('Taulukon pituus:', fruits.length);

let elem = document.querySelector('#heading');
console.log(elem);
console.dir(elem);
//elem.innerText = 'Mod2 esimerkit';

// taulukon looppaus eri tavoin
// perinteinen for
// yleinen tapa. Tarvitaan indeksi
console.log('--------------------')
console.log('Perinteinen FOR-looppi')

for (let i = 0; i < fruits.length; i++) {
    console.log(`Hedelmä ${i+1} on ${fruits[i]}`);
}

// Helppo ja nopea tapa iteroida ilman indeksiä

console.log('----------------------')
console.log('Läpikäynti for / of rakenteella, joilla saadaan arvot');

for (let fruit of fruits) {
    console.log(fruit);
}

// Harvemmin käytetään taulukoiden kanssa
// Js objektien kanssa jeba
console.log('----------------------')
console.log('Läpikäynti for / in rakenteella, joilla saadaan arvot ja index');
for (const index in fruits) {
    console.log(index, fruits[index]);
}


// Näin lisäät arrayhin tietoa:
//sort() sorts the array alphabetically
// reverse() reverses the items in the array in reverse order
fruits.sort()
console.log(fruits);
fruits.reverse()
console.log(fruits);

//ei toimi numeroiden kanssa

const ages = [2300, 28, 33, 19]
ages.sort();
console.log(ages);

//ages.sort(ages);

//tämä toimii numeroiden kanssa

/**const omafunktio = () => {
    console.log('Moi')
}
*/

ages.sort((a,b) => a - b)
console.log(ages);
ages.sort((a,b) => b - a);
console.log(ages)

let hedelmät = ['Banaani','Mango', 'Päärynä', 'Omena']
//shift() deletes and returns the 1st item in the array
const hedelmä = hedelmät.shift();
console.log('Poisetettiin', hedelmä)
console.log (hedelmät);
//unshift lisää taulukkoon alkuun
hedelmät.unshift('Kivi');
console.log(hedelmät)

// sama kuin shift mutta vika
const vika = hedelmät.pop();
console.log('Poisetettiin', vika)
console.log (hedelmät);

hedelmät.push('Satsuma', 'Mandariini');
console.log(hedelmät);

//includes tsekkaa onko arvo taulukossa ja palautttaa true/false
console.log(hedelmät.includes('Kivi'));

