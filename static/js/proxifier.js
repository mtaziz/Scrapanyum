function init() {
    // AJAX for client creation
    $('.connect').on('click', function (event) {
        event.preventDefault();
        id = $(this).attr('id');
        proxify(id);
    });

    function proxify(id) {
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            url: "proxifier_ajax",
            type: "POST",
            data: {
                id: id,
                csrfmiddlewaretoken: csrftoken,
            }
        });
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
