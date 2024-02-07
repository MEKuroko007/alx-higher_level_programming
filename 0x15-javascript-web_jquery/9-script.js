// JavaScript code that displays the value of hello

$(() => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (data, status) => {
    if (status === 'success') {
      $('div#hello').text(data.hello);
    }
  });
});
