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

$('.star-rating').each(function() {
    numberOfStars = $(this).data('rating');
    $(this).html = getStars(numberOfStars)
})