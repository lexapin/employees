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
      $("#keyboardModal").modal("hide");
    }
    else {
      alert("Выберите для теста хотя бы одну клавиатуру");
    }
  });
});