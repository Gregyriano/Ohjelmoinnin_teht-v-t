'use strict'


const form = document.querySelector('form#tvmaze');
const inputtext = form.querySelector('input[name="q"]');
const div = document.getElementById('tulokset');



form.addEventListener('submit', async function(event) {
    event.preventDefault();

    const haku = inputtext.value.trim();

    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${haku}`);
        const tulokset = await response.json();

        console.log('TVMaze search results:', tulokset);

        div.innerHTML = '';

        for (let tulos of tulokset) {
            const show = tulos.show;

            const article = document.createElement('article');

            const h2 = document.createElement('h2');
            h2.textContent = show.name;

            const link = document.createElement('a');
            link.href = show.url;
            link.target = '_blank';
            link.textContent = 'Linkki osoitteeseen';

            const img = document.createElement('img');
            img.src = show.image?.medium || '';
            img.alt = show.name;

            const summaryDiv = document.createElement('div');
            summaryDiv.innerHTML = show.summary || 'No summary available';

            article.appendChild(h2);
            article.appendChild(link);
            article.appendChild(img);
            article.appendChild(summaryDiv);

            div.appendChild(article);
        };

    } catch (error) {
        console.error('Error fetching data:', error);
    }
});