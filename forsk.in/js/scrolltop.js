$(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
        $("#rocketbacktotop").removeAttr("href"); $("#rocketbacktotop").stop().animate(
{ bottom: "0" }, { duration: 100, queue: false })
    }
    else {
        $("#rocketbacktotop").stop().animate({ bottom: "30000" },
{ duration: 8000, queue: false })
    } 
}); $(function () {
    $("#rocketbacktotop").click(function () {
        $("html, body").animate({ scrollTop: 0 }, "slow");
        return false
    })
});