(function () {
    "use strict";

    const $sliderWrap = $(".partners-slider-wrap");
    const $slider = $sliderWrap.find("#slider");
    let width = $(window).width();
    let slides;
    let slideWidth;
    if (width <= 645) {
        slides = 1;
        slideWidth = 320;
    } else if (width <= 1069) {
        slides = 2;
        slideWidth = 323;
    } else {
        slides = 3;
        slideWidth = 323;
    }

    $slider.bxSlider({
        slideWidth: slideWidth,
        minSlides: slides,
        maxSlides: slides,
        moveSlides: 1,
        slideMargin: 14,
        nextSelector: $sliderWrap.find("a.next"),
        prevSelector: $sliderWrap.find("a.prev"),
        nextText: '<i class="fa fa-long-arrow-right" aria-hidden="true"></i>',
        prevText: '<i class="fa fa-long-arrow-left" aria-hidden="true">',
        pager: false
    });


})();