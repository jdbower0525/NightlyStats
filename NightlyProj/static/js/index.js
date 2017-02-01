function list_data(){
    $.ajax({
        url: '/api/Day/1/',
        type: 'GET',
        datatype: 'json',
    }).done(function(results){
        var source = $('#day_results').html();
        var template = Handlebars.compile(source);
        var html = template(results);
        $('#stats1').append(html);
    })
}

list_data()
