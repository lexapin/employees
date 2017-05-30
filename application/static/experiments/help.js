$(function() {
  $(".menu").click(function(){
    // var pathname = window.location.pathname; // Returns path only
    // var url      = window.location.href;
    window.location.replace(window.location.href+"/"+$(this).attr("id"));
  })
})