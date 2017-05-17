$(function(){
  // keyboard form
  var key = false;
  var num = false;
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
  var keys = char_keys + num_keys;
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
});