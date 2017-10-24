$(function() {
  var draw = SVG('schema').size(250, 250);
  nodes[1] = create_node(draw, 20, 20, 1);
  nodes[2] = create_node(draw, 150, 20, 2);
  nodes[3] = create_node(draw, 150, 150, 3);
  nodes[4] = create_node(draw, 20, 150, 4);
  

  $('.my_button').click(function(event){
    for(node_id in nodes){
      change_fill(node_id, '#fff');
    }
    var local_stack = dict[parseInt(event.target.id)];
    console.log(local_stack);
    for (var i = 0; i < local_stack.length; i++) {
      change_fill(local_stack[i], '#f06');
    }
    stack = local_stack.slice();
  });
  

  $('.my_button').mouseenter(function(){
    if (current_danger){
      console.log('Have DANGER');
      $('#'+current_danger).removeClass('btn-danger').addClass('btn-info');
      current_danger = null;
    }else{
      console.log('NO DANGER');
    }
  });
});


var create_node = function(paper, x, y, id){
  element = paper.circle(50).fill('#fff').move(x, y);
  element.stroke({ color: '#f06', width: 5, linecap: 'round' });
  element.state = '#fff';
  element.node_id = id;
  element.on('mouseover', function() {
    this.fill({ color: '#f06' });
    update_stack(this.node_id, this.state, true);
  });
  element.on('mouseout', function() {
    this.fill({ color: this.state });
    update_stack(this.node_id, this.state, false);
  });
  element.on('click', function() {
    if(this.state=='#fff'){
      this.state='#f06';
    }else{
      this.state='#fff';
    }
    this.fill({ color: this.state });
  });
  return element;
}


var update_stack = function(node_id, state, in_object){
  if(state=='#fff'){
    if(in_object){
      stack.push(node_id);
      if (stack.length>2){
        value = stack.shift();
        change_fill(value, '#fff');
      }
    }
    else
      if (stack[0]==node_id)
        stack.shift();
      else
        stack.pop();
  }
  update_keypad();
}


var change_fill = function(node_id, fill){
  var node = nodes[node_id];
  node.state = fill;
  node.fill({ color: node.state });
}


var update_keypad = function(){
  var local_stack = stack.slice();
  local_stack.sort();
  console.log('hello', local_stack);
  for(key in dict){
    if (local_stack.equals(dict[key])){
      if(current_danger)
        $('#'+current_danger).removeClass('btn-danger').addClass('btn-info');
      current_danger = key;
      $('#'+current_danger).removeClass('btn-info').addClass('btn-danger');
      return
    }
  }
}

// Warn if overriding existing method
if(Array.prototype.equals)
    console.warn("Overriding existing Array.prototype.equals. Possible causes: New API defines the method, there's a framework conflict or you've got double inclusions in your code.");
// attach the .equals method to Array's prototype to call it on any array
Array.prototype.equals = function (array) {
  // if the other array is a falsy value, return
  if (!array)
    return false;

  // compare lengths - can save a lot of time 
  if (this.length != array.length)
    return false;

  for (var i = 0, l=this.length; i < l; i++) {
    // Check if we have nested arrays
    if (this[i] instanceof Array && array[i] instanceof Array) {
      // recurse into the nested arrays
      if (!this[i].equals(array[i]))
          return false;
    }
    else if (this[i] != array[i]) {
      // Warning - two different object instances will never be equal: {x:20} != {x:20}
      return false;
    }
  }
  return true;
}
Object.defineProperty(Array.prototype, "equals", {enumerable: false});

var stack = [];

var dict = {
  0: [],
  1: [1],
  2: [2],
  3: [3],
  4: [4],
  5: [1, 2],
  6: [1, 3],
  7: [1, 4],
  8: [2, 4],
  9: [3, 4],
}

var nodes = {}

var current_danger = null;