function init() {
    // AJAX for client creation
    $('#new_report_form').on('submit', function (event) {
        event.preventDefault();
        create_client();
    });

    function create_client() {
        var csrftoken = getCookie('csrftoken');

        var formData = new FormData();
        formData.append('mention_file', $('#id_mention_file')[0].files[0]);
        formData.append('tag_cloud_file', $('#id_tag_cloud_file')[0].files[0]);
        formData.append('top_twitter_file', $('#id_top_twitter_file')[0].files[0]);
        formData.append('first_name', $('#first_name_field').val());
        formData.append('last_name', $('#last_name_field').val());
        formData.append('brand', $('#brand_field').val());
        formData.append('trip_advisor', $('#tripadvisor_field').val());
        formData.append('twitter', $('#twitter_field').val());
        formData.append('facebook', $('#facebook_field').val());
        formData.append('query_name', $('#query_name_field').val());
        formData.append('query', $('#query_field').val());
        formData.append('csrfmiddlewaretoken', csrftoken);

        show_load();
        $.ajax({
            url: "create_client/",
            type: "POST",
            data: formData,

            processData: false,
            contentType: false,

            complete: function (data) {
                setTimeout(hide_load(data), 2000);
            },

            error: function () {
                console.log("Error sending AJAX");
            }
        });
    }

    // AJAX brandwatch query creator
    $('#create_bw_query').on('click', function (event) {
        event.preventDefault();
        create_bw_query();
    });

    function create_bw_query() {
        var csrftoken = getCookie('csrftoken');

        $.ajax({
            url: "bw_query_ajax/",
            type: "POST",
            data: {
                query_name: $('#query_name_field').val(),
                query: $('#query_field').val(),

                csrfmiddlewaretoken: csrftoken,
            },

            complete: function (data) {
                setTimeout(hide_load(data), 2000);
            },

            error: function () {
                console.log("Error sending AJAX");
            }
        });

        $.ajax({
            url: "refresh_templates/",
            data: {
                csrfmiddlewaretoken: csrftoken,
            },

            success: function (data) {
                $('#templates_accordion').html(data);
            },

            complete: function (data) {
                setTimeout(hide_load(data), 2000);
            },

            error: function () {
                console.log("Error sending AJAX");
            }
        });
    }


// AJAX refresh templates
// -------------------------------------------------------------------------------------------------------------------//

    function show_load() {
        $('.load_div').show();
    }

    function hide_load(data) {
        $('.load_div').hide();
    }


    // Method to add the Cross Site scxripting token defense for AJAX calls
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
