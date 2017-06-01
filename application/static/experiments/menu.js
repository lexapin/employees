$(function() {
  var max_depth = 4;
  var max_items = 5;
  var IMPERICAL = []; //Переменная для расчета времени по имперической формуле
  var menu = {
    name: "0",
    items: [],
    parent: null,
  };
  var menu_array = [menu];
  var randomINT = function(max) {
    var rand = Math.random() * (max);
    return Math.floor(rand);
  }
  var create_menu = function(local_menu, current_depth=1) {
    if (current_depth <= 4) {
      var items_count = 0;
      if (current_depth == 1 || current_depth == 2){
        items_count = 3;
      }
      items_count += randomINT(max_items);
      if (items_count > 0)
        for (var i = 0; i < items_count; i++) {
          var menu = {
            name: local_menu.name+"."+(i+1).toString(),
            items: [],
            parent: local_menu,
          }
          local_menu.items.push(menu);
          menu_array.push(menu);
          create_menu(menu, current_depth+1);
        }
    }
  }
  create_menu(menu);
  // Рисует случайное меню
  var insert_main_item = function(html_menu, item){
    var item_li = document.createElement('li');
    item_li.className = "dropdown";
    item_li.setAttribute("role", "presentation");
    item_li.innerHTML = '<a class="dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">' + 
      "Меню " + item.name.slice(2) + '<span class="caret"></span></a>';
    html_menu.append(item_li);
    var item_ul = insert_main_item_menu(item);
    item_li.appendChild(item_ul);
  };
  var insert_main_item_menu = function(item){
    var item_ul = document.createElement('ul');
    item_ul.id = "menu."+item.name.slice(2);
    item_ul.className = "dropdown-menu";
    item.items.forEach(function(sub_item){
      sub_item_li = document.createElement('li');
      sub_item_li.innerHTML = '<a href="#">'+ "Меню " + sub_item.name.slice(2) +'</a>';
      item_ul.appendChild(sub_item_li);
      if (sub_item.items.length>0){
        sub_item_li.className = "dropdown-submenu";
        sub_item_li.appendChild(insert_main_item_menu(sub_item));
      }
      else {
        sub_item_li.className = "hello";
        sub_item_li.id = sub_item.name
      }
    });
    return item_ul;
  };
  var html_menu = $("#menu-ul");
  menu.items.forEach(function(item){
    insert_main_item(html_menu, item);
  });
  var get_command_path = function(command){
    var command_name = "Меню " + command.name.slice(2);
    if(command.parent != null){
      IMPERICAL.push(command.parent.items.length);
      var path = get_command_path(command.parent);
      path.push(command_name);
      return path;
    }
    return [];
  }
  var rand_command = function(){
    var commands = menu_array.filter(function(item) {
      return item.items.length == 0;
    });
    command = commands[randomINT(commands.length)];
    var command_path = get_command_path(command);
    $("#rand_path").text("Выполните комманду меню: " + command_path.join(" / "));
    return command;
  }
  var command = rand_command();
  // experiment vars
  var max_experiments = 10;
  var count = 0;
  var CURRENT_RANDOM_COMMAND = null;
  var experiments = {};
  var imperic_exp = {};
  // Добавляем событие клавиши
  $('li.hello').click(function(){
    if($(this).attr("id") == CURRENT_RANDOM_COMMAND.name)
      close_experiment();
    else
      message_alert("Неправильно выбран пункт меню!");
  });
  // experiment management functions
  var start_experiment = function(){
    IMPERICAL = [];
    var command = rand_command();
    CURRENT_RANDOM_COMMAND = command;
    experiments[count] = Date.now();
  }

  var close_experiment = function(){
    experiments[count] = Date.now() - experiments[count];
    console.log(IMPERICAL);
    var sum = 0;
    IMPERICAL.forEach(function(digit){
      sum+=50+150*Math.log2(digit+1);
    });
    imperic_exp[count] = sum;
    count++;
    if (count<10)
      setTimeout(start_experiment, 500);
    else
      setTimeout(open_report, 500);
  }

  var open_report = function(){
    var data = [
      {
        x: _.keys(experiments),
        y: _.values(experiments),
        type: 'scatter',
        name: 'Экспериментальные значения'
      },
      {
        x: _.keys(experiments),
        y: _.values(imperic_exp),
        type: 'scatter',
        name: 'Эмперические значения'
      }
    ];

    Plotly.newPlot('myDiv', data);
    $("#reportModal").modal("show");
  }

  //Запуск эксперимента
  $("#menuModal").modal("show");
  $(".btn-primary").click(function(){
    $("#menuModal").modal("hide");
    start_experiment();
  });
});