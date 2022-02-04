/* Adapted from: https://codereview.stackexchange.com/questions/177945/convert-rating-value-to-visible-stars-using-fontawesome-icons/178069 */

function getStars(stars) {
    let output = [];
    for (let i = stars; i >= 1; i--) {
        output.push('<i class="fas fa-star"></i>');
    }
    for (let i = (5 - stars); i >= 1; i--) {
        output.push('<i class="far fa-star"></i>');
    }
    return output.join('');
}
let starClass = $('.star-rating');
console.log(getStars(4));

$.fn.stars = function() {
    return $(this).each(function() {
        const numberOfStars = $(this).data("rating");
        $(this).html = getStars(numberOfStars)
    });
}
/*
$(function(){
    $('.stars').stars();
});

$.each($('.star-rating'), function() {
    numberOfStars = $(this).data('rating');
    $(this).html = getStars(numberOfStars)
});

$('.star-rating').each(function() {
    numberOfStars = $(this).data('rating');
    $(this).html = getStars(numberOfStars)
})
*/