$(function() {
  $(".menu").click(function(){
    console.log(window.location.pathname); // Returns path only
    console.log(window.location.href);
    console.log(window.location.hostname);
    window.location.replace(window.location.hostname+"help/"+$(this).attr("id"));
  })
})