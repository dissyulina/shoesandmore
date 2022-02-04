
/* Prepopulate star rating on Edit Review Page */
const editStars = $('#edit-rating').data("editstars");
$( '#edit-rating input[ value=' + editStars + ']' ).attr('checked', 'checked');
