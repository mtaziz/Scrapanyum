function init() {

      // AJAX brandwatch query creator
    $('#refresh_categories').on('click', function (event) {
        event.preventDefault();
        refresh_categories();
    });

    function refresh_categories() {
        var csrftoken = getCookie('csrftoken');

        $.ajax({
            url: "/categorizer_ajax",
            // type: 'POST',
            data: {
                text_box: $('#id_text_box_field').val(),
                csrfmiddlewaretoken: csrftoken,
            },

            success: function (data) {
                console.log($('#id_text_box_field').val())
                $('.categorizer_results').html(data);
            },

            error: function () {
                console.log("Error sending AJAX");
            }
        });
    }



    // Method to add the Cross Site scripting token defense for AJAX calls
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

}

window.onload = init;
