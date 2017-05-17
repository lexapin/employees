$(function(){
  // keyboard form
  var key = false;
  var num = false;
  var experiment_keys = null;
  $("#keyCheckbox").prop("checked", key);
  $("#numCheckbox").prop("checked", num);
  $("#keyboardModal").modal("show");
  $(".btn-primary").click(function(){
    key = $("#keyCheckbox").prop("checked");
    num = $("#numCheckbox").prop("checked");
    if (!key && !num) {
      alert("Выберите для теста хотя бы одну клавиатуру");
    }
    else {
      $("#keyboardModal").modal("hide");
      experiment_keys = {};
      if (key)
        for (var key_char in char_keys)
          experiment_keys[key_char] = char_keys[key_char];
      if (num)
        for (var key_char in num_keys)
          experiment_keys[key_char] = num_keys[key_char];
      console.log("experiment_keys", _.keys(experiment_keys).length);
      console.log(key, num);
      start_experiment(_.keys(experiment_keys));
    }
  });
  // keyboard codes
  var char_keys = {
    49: "#path13",
    50: "#path15",
    51: "#path17",
    52: "#path19",
    53: "#path21",
    54: "#path23",
    55: "#path25",
    56: "#path27",
    57: "#path29",
    48: "#path31",
  };
  var num_keys = {
    97:  "#path175",
    98:  "#path177",
    99:  "#path179",
    100: "#path169",
    101: "#path171",
    102: "#path173",
    103: "#path163",
    104: "#path165",
    105: "#path167",
    96:  "#path373",
  };
  var keys = {};
  Object.assign(keys, char_keys);
  Object.assign(keys, num_keys);
  // svg
  var DEFAULT_FILL = "#97c5d5";
  var KEYDOWN_FILL = "#ff0000";
  var s = Snap("#svg");
  Snap.load("https://upload.wikimedia.org/wikipedia/commons/3/3a/Qwerty.svg", onSVGLoaded );
  function onSVGLoaded( data ){ 
    s.append( data );
    for (var key in keys) {
      var path_id = keys[key];
      console.log(path_id);
      Snap(path_id).attr({fill:DEFAULT_FILL})
    }
  }
  // experiment vars
  var max_experiments = 10;
  var count = 0;
  var CURRENT_RANDOM_CHAR = null;
  var experiments = {};
  // experiment functions
  var get_old_fill = function(snap_object){
    return DEFAULT_FILL
  }
  var keyDownTextField = function(e) {
    console.log("dshdfshn");
    var keyCode = e.keyCode;
    console.log(event.keyCode, String.fromCharCode(event.which));
    if (CURRENT_RANDOM_CHAR == keyCode) {close_experiment();}
    console.log("ВЫШЕЛ");
  }

  document.addEventListener("keyup", keyDownTextField, false);

  var randomChar = function(chars) {
    max = chars.length
    var rand = Math.random() * (max);
    rand = Math.floor(rand);
    return chars[rand];
  }

  var start_experiment = function(chars){
    var char = randomChar(chars);
    var char_id = experiment_keys[char];
    var snap_object = Snap(char_id)
    DEFAULT_FILL = get_old_fill(snap_object)
    snap_object.attr({ fill: "#ff0000" });
    CURRENT_RANDOM_CHAR = char;
    experiments[count] = Date.now();
  }

  var close_experiment = function(){
    experiments[count] = Date.now() - experiments[count];
    count++;
    if (count<10)
      setTimeout(start_experiment, 500, _.keys(experiment_keys));
    else
      setTimeout(open_report, 500);
    var char_id = experiment_keys[CURRENT_RANDOM_CHAR];
    var snap_object = Snap(char_id);
    snap_object.attr({ fill: DEFAULT_FILL });
  }

  var open_report = function(){
    console.log(experiments);
    var data = [
      {
        x: _.keys(experiments),
        y: _.values(experiments),
        type: 'scatter'
      }
    ];

    Plotly.newPlot('myDiv', data);
  }
});