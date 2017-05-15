(function($){
  $(function(){

    $('.button-collapse').sideNav();
    $('.parallax').parallax();


    $('.grid').masonry({
      // options
      itemSelector: '.card',
      columnWidth: 600,
      gutter: 20,
      horizontalOrder: true
    });

    $(".icon-block").on('click',function (e) {

	    var go = $(this).attr('go');
	    var $target = $(go);

	    $('html, body').stop().animate({
	        'scrollTop': $target.offset().top
	    }, 900, 'swing', function () {
	        window.location.hash = target;
	    });
	});

  }); // end of document ready
})(jQuery); // end of jQuery name space
