function search_client() {
    var search = $('#client_search').val()
    var data = {
        search: search
    };
    $.ajax({
        url: '/refresh_clients/',
        data: data,
        success: function (data, status, xhr) {
            console.log("returning" + data)
            $("#client_list").html(data)
        }
    });
    $('#business_list').html('')
}

function search_business() {
    var search = $('#business_search').val()
    var data = {
        search: search
    };
    $.ajax({
        url: '/refresh_business/',
        data: data,
        success: function (data, status, xhr) {
            console.log("returning" + data)
            $("#business_list").html(data)
        }
    });
    $('#client_list').html('')
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

// select clients or business form list
function select_client(i) {
    $('.current_selected_client').removeClass('btn-success').removeClass('current_selected_client');
    $('#' + i.id).addClass('btn-success').addClass('current_selected_client');
    $('#final_client').html(i.innerHTML)
}

function select_business(i) {
    $('.current_selected_business').removeClass('btn-success').removeClass('current_selected_business');
    $('#' + i.id).addClass('btn-success').addClass('current_selected_business');
    $('#final_business').html(i.innerHTML)
}


// AJAX for client creation
function create_client() {
    var csrftoken = getCookie('csrftoken');

    var formData = new FormData();
    formData.append('DNI', $('#DNI_field').val());
    formData.append('name', $('#name_field').val());
    formData.append('address', $('#address_field').val());
    formData.append('telephone', $('#telephone_field').val());
    formData.append('email', $('#email_field').val());
    formData.append('legalitas_id', $('#legalitas_id_field').val());

    formData.append('csrfmiddlewaretoken', csrftoken);

    $.ajax({
        url: "create_client_ajax/",
        type: "POST",
        data: formData,

        processData: false,
        contentType: false,

        complete: function (data) {
            console.log("Creating client");
            search_client()
        },

        error: function () {
            console.log("Error sending AJAX for client");
        }
    });
}


// AJAX for business creation
function create_business() {
    var csrftoken = getCookie('csrftoken');

    var formData = new FormData();

    formData.append('client', $('#id_client').val());
    formData.append('brand', $('#brand_field').val());
    formData.append('NIF', $('#NIF_field').val());
    formData.append('owner_name', $('#owner_name_field').val());
    formData.append('business_address', $('#business_address_field').val());
    formData.append('business_telephone', $('#business_telephone_field').val());
    formData.append('business_email', $('#business_email_field').val());
    formData.append('web_url', $('#web_url_field').val());

    formData.append('csrfmiddlewaretoken', csrftoken);

    $.ajax({
        url: "create_business_ajax/",
        type: "POST",
        data: formData,

        processData: false,
        contentType: false,

        complete: function (data) {
            console.log("Creating business");
            search_business()
        },

        error: function () {
            console.log("Error sending AJAX for business");
        }
    });
}

// AJAX for batch creation
function create_batch() {
    var csrftoken = getCookie('csrftoken');

    var formData = new FormData();
    formData.append('csrfmiddlewaretoken', csrftoken);

    formData.append('client', $('#final_client').html());
    formData.append('business', $('#final_business').html());
    formData.append('start', $('#start_field').val());
    formData.append('end', $('#end_field').val());
    formData.append('legalitas_batch', $('#legalitas_batch_field').val());

    if ($("#idm_tab").is(":visible")) {
        instance_type = "idm"
        formData.append('trip_advisor', $('#tripadvisor_url_field').val());
        formData.append('google', $('#google_url_field').val());
        formData.append('facebook', $('#facebook_url_field').val());
    } else if ($("#mail_alerts_tab").is(":visible")) {
        instance_type = "mail_alerts"
        formData.append('client_email', $('#alert_email_field').val());
    } else if ($("#proxifier_tab").is(":visible")) {
        instance_type = "proxifier"
    }

    formData.append('instance_type', instance_type);

    $.ajax({
        url: "create_batch_ajax/",
        type: "POST",
        data: formData,

        processData: false,
        contentType: false,

        success: function (data) {
            console.log(formData);

            $.notify({
                // options
                message: 'Tarea creada correctamente!',
                placement: {
                    from: "bottom",
                    align: "left"
                }
            }, {
                // settings
                type: 'success'
            });

            $('#batch_form').trigger("reset");

        },

        error: function () {
            console.log("Error sending AJAX");

            $.notify({
                // options
                message: 'No se pudo crear la tarea...!',
                placement: {
                    from: "bottom",
                    align: "left"
                }
            }, {
                // settings
                type: 'danger'
            });
        }
    });
}

// Delete business AJAX
function delete_business() {
    var csrftoken = getCookie('csrftoken');
    business_id = $('#final_business').html();

    var formData = new FormData();
    formData.append('csrfmiddlewaretoken', csrftoken);
    formData.append('business_id', business_id);

    $.ajax({
        url: "delete_business_ajax/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,

        complete: function (data) {
            search_business()
        },

        error: function () {
            console.log("Error sending AJAX");
        }
    });
}


// Delete client AJAX
function delete_client() {
    var csrftoken = getCookie('csrftoken');
    client_id = $('#final_client').html();

    var formData = new FormData();
    formData.append('csrfmiddlewaretoken', csrftoken);
    formData.append('client_id', client_id);

    $.ajax({
        url: "delete_client_ajax/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,

        complete: function (data) {
            search_client()
        },

        error: function () {
            console.log("Error sending AJAX");
        }
    });
}