function getCookie(name) {
   var cookieValue = null;
   if (document.cookie && document.cookie !== '') {
       var cookies = document.cookie.split(';');
       for (var i = 0; i < cookies.length; i++) {
           var cookie = jQuery.trim(cookies[i]);
           if (cookie.substring(0, name.length + 1) === (name + '=')) {
               cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
               break;
           }
       }
   }
   return cookieValue;
}


var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
   return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


function inputDay(e){
    e.preventDefault()
    var date = $("#date").val()
    var net_sales = $("#net_sales").val()
    var forecast = $("#forecast").val()
    var food_sales = $("#food_sales").val()
    var beverage_sales = $("#beverage_sales").val()
    var context = {
        username: userName,
        password: userPassword,
        first_name: firstname,
        last_name: lastname,
        email: emailAddress,
    }
    $.ajax({
        url: '/api/User/',
        type: 'POST',
        data: context
    }).done(function(results){
        createEmbarker(results.id)
    })
}
$("#inputDay").click(inputDay)
