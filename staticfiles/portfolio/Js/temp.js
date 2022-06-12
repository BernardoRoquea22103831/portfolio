const options = {
    method: 'GET',
    headers: {
        'X-RapidAPI-Key': 'd3e8f37b24msh6f5fa9edb567ad7p1861ebjsn2db6f92a83df',
        'X-RapidAPI-Host': 'daily-cat-facts.p.rapidapi.com'
    }
};

fetch('https://daily-cat-facts.p.rapidapi.com/facts/random?amount=5', options)
    .then(response => response.json())
    .then(response =>{
        document.getElementById('id').innerHTML= response[2].text;
    })
    .catch(err => console.error(err));