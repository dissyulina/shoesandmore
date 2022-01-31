// Country field
let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
}); 

// Hover on ratings
$(".fa-star").mouseenter(function(){
    $(this).removeClass("far").addClass("fas");
    $(this).parent().prevAll().children('.fa-star').removeClass("far").addClass("fas");
    $(".fa-star").mouseleave(function(){
        $(this).removeClass("fas").addClass("far");
        $(this).parent().prevAll().children('.fa-star').removeClass("fas").addClass("far");
    });
});
