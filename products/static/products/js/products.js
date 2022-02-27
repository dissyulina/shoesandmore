$(document).ready(function() {
    // Back to top button functionality
    $("#back-to-top").click(function(event) {
        event.preventDefault();
        $("html, body").animate({ scrollTop: 0 });
        return false;
    });

    // Turn Add to favorite button (heart icon) into red
    $('.fa-inverse').hover(function(){
        $(this).toggleClass("text-danger");
    });
    $('.fa-inverse').click(function(){
        $(this).focus();
    });
});