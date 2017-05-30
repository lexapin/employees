$(function() {
  $(".menu").click(function(){
    console.log(window.location.pathname); // Returns path only
    console.log(window.location.href);
    window.location.replace(window.location.href+"/"+$(this).attr("id"));
  })
})