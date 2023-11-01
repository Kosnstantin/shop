$(document).ready(function () {
    let good_pk = window.location.pathname.split('/').pop()
    $('#good_info').click(function () {
        $.ajax({
            url: '/good_info/' + good_pk + '/',
            dataType: 'json',
            success: function (data) {
                $('#content').html(data.data);
            }
        });
    });
    $('#characteristics').click(function () {
        $.ajax({
            url: '/characteristics/' + good_pk + '/',
            dataType: 'json',
            success: function (data) {
                $('#content').html(data.data);
            }
        });
    });
    $('#add_review').click(function () {
        $.ajax({
            url: '/add_review/' + good_pk + '/',
            dataType: 'json',
            success: function (data) {
                $('#content').html(data.data);
            }
        });
    });
});