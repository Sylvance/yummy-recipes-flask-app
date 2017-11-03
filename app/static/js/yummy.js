$( document ).ready(function() {
    // setTimeout() function will be fired after page is loaded
    // it will wait for 5 sec. and then will fire
    // $("#yummy-flash").hide() function
    setTimeout(function() {
        $("#yummy-flash").hide('blind', {}, 500)
    }, 5000);
});