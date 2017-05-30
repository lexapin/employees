$(function() {
  $(".menu").click(function(){
    console.log(window.location.pathname); // Returns path only
    console.log(window.location.href);
    console.log(document.domain);
    window.location.replace("http://"+document.domain+"/help/"+$(this).attr("id"));
  })
})