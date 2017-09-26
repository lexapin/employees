$(function(){
  $("#solve").click(function(){
    var x1 = $("#x1").val();
    var x2 = $("#x2").val();
    var x3 = $("#x3").val();
    var x4 = $("#x4").val();
    var x5 = $("#x5").val();
    var x6 = $("#x6").val();
    var x7 = $("#x7").val();
    var arr = [x1, x2, x3, x4, x5, x6, x7];
    for (var x in arr){
      var value = arr[x];
      if(value) arr[x] = parseFloat(value);
    }
    var z=-3.74-0.14*arr[0]-0.36*arr[1]+0.16*arr[2]+0.69*arr[3]+0.02*arr[4]-1.03*arr[5]+0.79*arr[6];
    console.log(z);
    var p = 1.0/(1.0+Math.exp(-z))*100;
    var description;
    if (p>20) description = "Высокий риск несостоятельности швов колоректального рака";
    else description = "Низкий риск развития несостоятельности швов колоректального анастомоза";
    $("#result").append("<h3>"+p.toFixed(2)+"%"+"<br>"+description+"</h3>);
    $("#reportModal").modal("show");
  });
})