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
  // svg
  var DEFAULT_FILL = "#97c5d5";
  var KEYDOWN_FILL = "#ff0000";
  var s = Snap("#svg");
  Snap.load("https://upload.wikimedia.org/wikipedia/commons/3/3a/Qwerty.svg", onSVGLoaded );
  function onSVGLoaded( data ){ 
    s.append( data );
    for (var key in keys) {
      var path_id = keys[key];
      Snap(path_id).attr({fill:DEFAULT_FILL})
    }
  }
});