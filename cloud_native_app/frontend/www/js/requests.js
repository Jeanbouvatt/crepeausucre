var url = 'http://0.0.0.0'

var check = function(id) {
  $.get(url + ':8091/link/' + id)
  .done(function(data) {
    console.log(data);
  })
  .fail(function(error) {
    console.log(error);
    $('#check_played').html('Erreur lors de la récupération des informations : <pre>' + error.statusText + '</pre>');
  });
}

var get_link = function(id) {
  $.get(url + ':8092/get_button/' + id)
  .done(function(data) {
    console.log(data);
    $("#play_link").html('<a href="' + link + '">Cliquez ici pour jouer !</a>');
  })
  .fail(function(error) {
    console.log(error);
    $('#play_link').html('Erreur lors de la récupération des informations : <pre>' + error.statusText + '</pre>');
  });
}

var get_id = function() {
  return prompt('Quelle est votre identifiant de joueur ? Nouveau joueur, laissez vide.') || 10;
}

var launch = function() {
  id = get_id();
  check(id);
  get_link(id);
}

$('#play_link').html('Erreur lors de la récupération des informations : ');
launch();

