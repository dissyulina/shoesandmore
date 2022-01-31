// Hover on ratings
$(".fa-star").mouseenter(function(){
    $(this).removeClass("far").addClass("fas");
    $(this).parent().prevAll().children('.fa-star').removeClass("far").addClass("fas");
    $(".fa-star").mouseleave(function(){
        $(this).removeClass("fas").addClass("far");
        $(this).parent().prevAll().children('.fa-star').removeClass("fas").addClass("far");
    });
});
