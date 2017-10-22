var chars = "ёйцукенгшщзхъфывапролджэячсмитьбю"+"qwertyuiopasdfghjklzxcvbnm";

function analise(argument) {
  var text = $('#textarea').val().toLowerCase();
  var chars_freq = {};
  for (var i = 0; i < text.length; i++) {
    if (chars.includes(text[i]))
      if (chars_freq.hasOwnProperty(text[i])){
        chars_freq[text[i]]+=1;
      }else{
        chars_freq[text[i]]=1;
      }
  }
  for(key in chars_freq){
    chars_freq[key]=chars_freq[key]/text.length;
  }
  sorted_keys = Object.keys(chars_freq).sort(function(a,b){return chars_freq[b]-chars_freq[a]})
  console.log(sorted_keys);
  console.log(chars_freq);
  var data = [];
  var sorted_values = [];
  for (var i = 0; i < sorted_keys.length; i++) {
    data.push({
      char: sorted_keys[i],
      freq: chars_freq[sorted_keys[i]]
    });
    sorted_values.push(chars_freq[sorted_keys[i]]);
  }
  $('#freq_table').bootstrapTable({
    data: data
  });
  $('#div_table').css('visibility', 'visible');
  var plot_data = [
    {
      x: sorted_keys,
      y: sorted_values,
      type: 'bar'
    }
  ];
  Plotly.newPlot('bar_chart', plot_data);
}
