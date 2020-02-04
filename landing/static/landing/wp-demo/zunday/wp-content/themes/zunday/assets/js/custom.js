"use strict";
jQuery(document).ready(function ($) {

/*--------------------------------------------------------------
# navigation button
--------------------------------------------------------------*/
 $('.n_button').on("click",function(){
   $(this).find("#nav-icon2").toggleClass('open');
   $(".mainMenuOpCnt").toggleClass("openMenu");
   $(".sideTB").addClass("sideOpened");
 });


 $('.closeMenu').on("click",function(){
    $("#nav-icon2").removeClass('open');
    $(".mainMenuOpCnt").removeClass("openMenu");
    $(".sideTB").removeClass("sideOpened");

 }); 


/*--------------------------------------------------------------
# menu toggle function
--------------------------------------------------------------*/
$('.menu--zunday > ul > li.menu-item-has-children > a').on("click",function(e){

  e.preventDefault();

    var $this = $(this);

    $(".menu--zunday > ul > li > a").removeClass("currentMenuItem");  

    $this.addClass("currentMenuItem");

});

$('.menu--zunday .menu-item-has-children > a').on("click",function(e){
  	e.preventDefault();
  
    var $this = $(this);

    $(".menu--zunday .menu > ul > li > a").removeClass("currentMenuItem");
  
    $this.addClass("currentMenuItem");

    if ($this.next().hasClass('show')) {
        $this.next().removeClass('show');
        $this.next().slideUp(350);
    } else {
        $this.parent().parent().find('li .sub-menu').removeClass('show');
        $this.parent().parent().find('li .sub-menu').slideUp(350);
        $this.parent().parent().find('li .sub-menu a').removeClass("currentMenuItem");
        $this.next().toggleClass('show');
        $this.next().slideToggle(350);
    }
});


$('a.searchBtns').on("click",function(e){
    e.preventDefault();

    $(".srcDv").toggleClass("openedSa");

});


  /*--------------------------------------------------------------
  # Slider
  --------------------------------------------------------------*/
  $('#slider').bxSlider({
      mode: 'fade',
      auto: false,
    });


  /*--------------------------------------------------------------
  # box effect
  --------------------------------------------------------------*/
  AOS.init({
    easing: 'ease-in-out-sine',
    disable: 'mobile',
  });
    

  $(".my-gallery").lightGallery({
    selector: '.bgImageFgallery'
}); 


});


jQuery(window).load(function () {
  jQuery(".spinnerCont").remove();
});



