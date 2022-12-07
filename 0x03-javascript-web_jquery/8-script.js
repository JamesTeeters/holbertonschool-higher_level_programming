$.get('https://swapi-api.hbtn.io/api/films/?format=json', (content) => {
  const movielist = content.results;
  $.each(movielist, (key, value) => {
    $('#list_movies').append('<li>' + value.title + '</li>');
  });
});
