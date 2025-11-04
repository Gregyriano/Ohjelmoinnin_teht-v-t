/**
   Tässä tiedostossa on
   ensimmäisiä JavaScript-
   esimerkkejä
   */
    'use strict';


    // Käytä const-avainsana muuttujan esittelyyn, paitsi jos sen arvoa
    // tarttee myöhemmin muuttaa
    let teksti = 'Moi maailma!'


   console.log('I have awaken')
    console.log(teksti);
    teksti = 'Moi Matti!';

    // Selaimen oma alert-ikkuna (popup)
   // alert('Kukkuu!')
    document.querySelector('.output').textContent = teksti;

    let name = 'Matti';
    let age = 23;
    let greeting = `Moi ${name},${age}!`;
    console.log(greeting);

    //syötteen lukeminen
    name = prompt('Anna nimesi:');
   // console.log('Käyttäjän syöte', userInput);
   age = parseInt(prompt('Anna ikäsi:'));

   if (10 < age && age <  100) {
    greeting = `Moi ${name}, ikäsi vuoden päästä ${age + 1}!`;
    document.querySelector('.output').textContent = teksti;
   } else {
       console.log('Olet liian nuori tälle sivulle');
   }

    //Math - luokka
// noppaesimerkki
   const result = Math.ceil(Math.random()*6);
   console.log('noppaheitto', result);

   switch (result) {
       case 6:
           console.log("Voitit 100 euroa");
           break;
       case 5:
           console.log("Voitit 50!");
           break;
       case 4:
           console.log("Voitit 20 e");
           break;
       default:
           console.log("et voittanut mitään")
   }

