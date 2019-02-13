$(window).on("load", function(){
  $('#preload').delay(4000).fadeOut('slow', function(){
     $(this).remove();
  });
});
