$(function(){
  draw = SVG('paper').size(640, 480);
  draw.on('click', function(event){
    if(can_add_point){
      var point = create_point(event.offsetX, event.offsetY);
      create_line(point);
      points.push(point);
    }
  });

  var create_point = function(x, y){
    var paper = draw;
    var radius = 5;
    var point = paper.circle(radius*2).fill('#f06').move(x-radius, y-radius);
    point.pid = get_point_id();
    point.on('click', function(){
      if(point.pid==0){
        create_line(this);
        points.push(this);
        can_add_point = false;
        if(analyse())
          alert('Выпуклый');
        else
          alert('Вогнутый');
      }
    })
    return point;
  }

  var get_point_id = function(){
    return points.length
  }

  var create_line = function(pb){
    var paper = draw;
    var last_index = points.length-1;
    if(last_index<0)
      return;
    var pa = points[last_index];
    line = paper.line(pa.attr('cx'), pa.attr('cy'), pb.attr('cx'), pb.attr('cy'));
    line.stroke({ color: '#f06', width: 1, linecap: 'round' })
  }

  $('#clear').on('click', function(){
    draw.clear();
    points = [];
    can_add_point = true;
  });
});

var points = [];
var can_add_point = true;
var draw = null;

function analyse() {
  console.log('Go to analyse', points.length);
  for (var i = 0; i < points.length-1; i++) {
    var a = points[i];
    var b = points[i+1];
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
      if(z(c.attr('cx'), c.attr('cy'))>=0)
        left_side.push(c);
      else
        right_side.push(c);
      if((left_side.length>0)&&(right_side.length>0))
        return false;
    }
  }
  return true;
}

