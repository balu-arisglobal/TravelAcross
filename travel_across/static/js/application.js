$(document).ready(function(){
    $('#home_div').show();
        $('#travel_detais').hide();
        $('#user_details').hide();
        $('#about_us').hide();

    $('#home').click(function(){
        $('#home_div').show();
        $('#travel_detais').hide();
        $('#user_details').hide();
        $('#about_us').hide();
    });

    $('#tdetails').click(function(){
        $('#travel_detais').show();
        $('#home_div').hide();
        $('#user_details').hide();
        $('#about_us').hide();
    });

    $('#udetails').click(function(){
        $('#user_details').show();
        $('#travel_detais').hide();
        $('#home_div').hide();
        $('#about_us').hide();
    });

    $('#about').click(function(){
        $('#about_us').show();
        $('#travel_detais').hide();
        $('#user_details').hide();
        $('#home_div').hide();
    });
});