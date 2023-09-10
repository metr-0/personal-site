$(document).ready(function () {
    const link = $('.item-link');

    link.hover(function () {
        $(this).stop().animate({
            scale: 1.05,
            rotate: '2deg'
        }, 'fast');
    }, function () {
        $(this).stop().animate({
            scale: 1,
            rotate: '0deg'
        }, 'fast');
    });
});
