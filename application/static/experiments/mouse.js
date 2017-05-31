$(function(){
  $("#mouseModal").modal("show");
  $(".btn-primary").click(function(){
    if (false) {
      alert("Параметры выбраны неправильно");
    }
    else {
      $("#keyboardModal").modal("hide");
      start_experiment();
    }
  });
  // функции для проведения эксперимента
  var random_button_width = true;
  var random_button_height = true;
  var ccp = 0; //current circle position
  var cbp = 0; //current button position
  var circle_position = {
    0: {top: [240, 240], left: [540, 540]},
    1: {top: [100, 380], left: [100, 100]},
    2: {top: [100, 100], left: [100, 540]},
    3: {top: [100, 380], left: [540, 540]},
    4: {top: [380, 380], left: [100, 540]},
  }
  var button_position = {
    0: {top: function(){return 230+"px";}, left: function(){return get_random_position(50,300)+"px";}},
    1: {top: function(){return 50+"px";}, left: function(){return 50+"px";}},
    2: {top: function(){return 50+"px";}, left: function(){return 540+"px";}},
    3: {top: function(){return 380+"px";}, left: function(){return 50+"px";}},
    4: {top: function(){return 380+"px";}, left: function(){return 540+"px";}},
  }
  var get_random_position = function(min, max){
    var length = max-min;
    var rand = Math.random() * (length);
    return Math.floor(min+rand);
  }
  var create_start_position = function(){
    var circle = document.createElement('div');
    circle.className = "btn-circle";
    circle.style.top = get_random_position(circle_position[ccp].top[0], circle_position[ccp].top[1])-25+"px";
    circle.style.left = get_random_position(circle_position[ccp].left[0], circle_position[ccp].left[1])-25+"px";
    circle.innerHTML = "MOVE HERE";
    circle.addEventListener("mouseenter", function(){
      var top = parseInt($(this).css("top"));
      var left = parseInt($(this).css("left"));
      $(this).animate({
          width: "10px",
          height: "10px",
          left: left+20+"px",
          top: top+20+"px",
          "font-size": "1%",
          "line-height": "10px",
        }, 200, do_when_animation_complete);
      });
    $("#mouse").append(circle);
  }
  var click_on_button = function(){
    console.log("clicked");
    $(this).remove();
    close_experiment();
  }
  var create_button = function(){
    var button = document.createElement('div');
    button.className = "button";
    button.innerHTML = "<a href='#'>click me</a>";
    button.style.left = button_position[cbp].left();
    button.style.top = button_position[cbp].top();
    if (random_button_width) button.style.width = get_random_position(50, 90)+"px";
    if (random_button_height) {
      var height = get_random_position(20, 40);
      var top = parseInt(button.style.top);
      button.style.height = height+"px";
      button.style.top = (top-height/2)+"px";
      button.style["line-height"] = height+"px";
    }
    button.addEventListener("click", click_on_button);
    $("#mouse").append(button);
  }
  var do_when_animation_complete = function() {
    $(this).remove();
    create_button();
  }
  // переменные эксперимента
  var max_experiments = 10;
  var count = 0;
  var experiments = {};
  // управление экспериментом
  var start_experiment = function(chars){
    // start experiment
    ccp = get_random_position(1,4);
    cbp = get_random_position(1,4);
    create_start_position();
    experiments[count] = Date.now();
  }

  var close_experiment = function(){
    experiments[count] = Date.now() - experiments[count];
    count++;
    if (count<max_experiments)
      setTimeout(start_experiment, 500);
    else
      setTimeout(open_report, 500);
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
    $("#reportModal").modal("show");
  }
});