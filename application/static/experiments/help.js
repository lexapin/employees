$(function() {
  $(".menu").click(function(){
    window.location.replace("http://"+document.domain+"/help/"+$(this).attr("id"));
  });
  $("p.search").click(function(){
    window.location.replace("http://"+document.domain+"/help/"+$(this).attr("id"));
  });
})