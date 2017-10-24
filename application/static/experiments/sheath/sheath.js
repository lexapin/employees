$(function(){
  draw = SVG('paper').size(640, 480);
  draw.on('click', function(event){
    var point = create_point(event.offsetX, event.offsetY);
    points.push(point);
    create_sheath(point);
  });

  var create_point = function(x, y){
    var paper = draw;
    var radius = 5;
    var point = paper.circle(radius*2).fill('#f06').move(x-radius, y-radius);
    point.pid = get_point_id();
    return point;
  }

  var get_point_id = function(){
    return points.length
  }

  var create_sheath = function(pb){
    var paper = draw;
    if (points.length>3){
      var h = find_sheath();
      console.log(h);
      draw_lines(h);
    }
    // var last_index = points.length-1;
    // if(last_index<0)
    //   return;
    // var pa = points[last_index];
    // line = paper.line(pa.attr('cx'), pa.attr('cy'), pb.attr('cx'), pb.attr('cy'));
    // line.stroke({ color: '#f06', width: 1, linecap: 'round' })
  }

  $('#clear').on('click', function(){
    draw.clear();
    points = [];
    lines = [];
  });
});

var points = [];
var lines = [];
var draw = null;


function draw_lines(h){
  for (var i = 0; i < lines.length; i++) {
    lines[i].remove();
  }
  lines = [];
  for (var i = 0; i < h.length-1; i++) {
    var a = h[i];
    var b = h[i+1];
    create_line(a, b);
  }
}


var create_line = function(a, b){
  var paper = draw;
  var pa = points[a];
  var pb = points[b];
  line = paper.line(pa.attr('cx'), pa.attr('cy'), pb.attr('cx'), pb.attr('cy'));
  line.stroke({ color: '#f06', width: 1, linecap: 'round' });
  console.log(line);
  lines.push(line);
}


function find_sheath() {
  var minI = 0; //номер нижней левой точки
  var min = points[0].attr('cx');
  // ищем нижнюю левую точку
  for (var i = 1; i < points.length; i++) {
    if (points[i].attr('cx') < min) {
      min = points[i].attr('cx');
      minI = i;
    }
  }
  var a = points[minI];
  var sheath = [a.pid];
  // console.log('left point is ', a.pid);
  while(true){
  // строим вектора
  // ищем те у которых точки находятся левее всего
    // console.log('iteration');
    var b=null;
    for (var i = 0; i < points.length; i++) {
      b = points[i];
      if(sheath.length>1&&b.pid==sheath[sheath.length-2]){
        // console.log('  find this node in last iteration ', b.pid);
        continue;
      }
      if(b.pid==sheath[sheath.length-1]){
        // console.log('  this is am ', b.pid);
        continue;
      }
      if(find_line(a, b)){
        // console.log('  next line is ', a.pid, b.pid);
        break;
      }
    }
    // console.log('  find node ', b.pid);
    // debugger;
    sheath.push(b.pid);
    a = b;
    if(a.pid==sheath[0]){
      // console.log('  sheath complete');
      break;
    }
    if(sheath.length>20){
      // console.log('  maximum iterations');
      break;
    }
  }
  return sheath;
}

function find_line(a, b){
  var xa = a.attr('cx');
  var ya = a.attr('cy');
  var xb = b.attr('cx');
  var yb = b.attr('cy');
  var z = function(x,y){
    return (ya-yb)*x+(xb-xa)*y+(xa*yb-xb*ya);
  }
  var left_side = [];
  var right_side = [];
  for (var j = 0; j < points.length; j++) {
    var c = points[j];
    if(c==a||c==b){
      continue;
    }
    // console.log('  find_line', c.pid, z(c.attr('cx'), c.attr('cy')));
    if(z(c.attr('cx'), c.attr('cy'))>=0)
      left_side.push(c);
    else
      right_side.push(c);
    if((left_side.length>0)&&(right_side.length>0))
      return false;
  }
  return true;
}