// Country field
let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
}
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
}); 

// Review pill: If there's no item to be reviewed
$(document).ready(function(){
    let itemToBeReviewed = $('.item-to-be-reviewed').length;
    if (itemToBeReviewed === 0) {
        $('#reviews').html("<p>No items to be reviewed.</p>");
    }
});

/* Keep the current pill active on page reload */
$(document).ready(function(){
    $('a[data-bs-toggle="pill"]').click(function(e) {
        sessionStorage.setItem('activePill', $(e.target).attr('href'));
    });

    let activePill = sessionStorage.getItem("activePill");
    if (activePill) {
        $('#profile-pills a[href="' + activePill + '"]').addClass("active");
        let activeContent = activePill.substring(1);
        $('#' + activeContent).addClass("show active");
    } else {
        $('#profile-pills a[href="#information"]').addClass("active");
        $('#information').addClass("show active");
    }
});
