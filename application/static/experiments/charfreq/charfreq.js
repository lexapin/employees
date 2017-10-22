var chars = "ёйцукенгшщзхъфывапролджэячсмитьбю"+"qwertyuiopasdfghjklzxcvbnm";

function analise(argument) {
  var text = $('#textarea').val().toLowerCase();
  var result = {};
  for (var i = 0; i < text.length; i++) {
    if (chars.includes(text[i]))
      if text[i] in 
      result+=text[i];
  }
  $('#graph').html(result);
}