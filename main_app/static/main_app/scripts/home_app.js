jQuery(function ($) {
    $('.product-slick').slick({
    });
    // using $ here will be safely even jQuery.noConflict() will be enabled
    
});

jQuery(function ($) {
    $('.image-slick').slick({
        dots: true,
        slidesToShow: 2,
        slidesToScroll: 2,
        infinite: false,
    });
    // using $ here will be safely even jQuery.noConflict() will be enabled
    
});

jQuery(function ($) {
    $('.member-slick').slick({
        dots: true,
        slidesToShow: 1,
        slidesToScroll: 1,
    });
    // using $ here will be safely even jQuery.noConflict() will be enabled
    
});