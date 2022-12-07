$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (content) => {
    $('#hello').text(content.hello);
  });
});
