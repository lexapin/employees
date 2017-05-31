$(function() {
  $(".menu").click(function(){
    window.location.replace("http://"+document.domain+"/help/"+$(this).attr("id"));
  });
  $("p.class").click(function(){
    window.location.replace("http://"+document.domain+"/help/"+$(this).attr("id"));
  });
})