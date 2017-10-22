$(function() {
  $('#5').removeClass('btn-info').addClass('btn-danger');
  $('.my_button').click(function(event){
    console.log(event);
  });
  $('.my_button').mouseenter(function(){
    if ($('#5').hasClass('btn-danger')){
      console.log('Have DANGER');
      $('#5').removeClass('btn-danger').addClass('btn-info');
    }else{
      console.log('NO DANGER');
    }
  });
});
