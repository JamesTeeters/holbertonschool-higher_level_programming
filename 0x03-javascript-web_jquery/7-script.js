$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (content) => {
    $('#character').txt(content.name);
});
