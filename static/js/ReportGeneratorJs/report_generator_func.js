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

function show_load(id) {
    if ($('#load_div_' + id).css('display') == "none") {
        $('#load_div_' + id).show();
    }
}


function generate_AJAX(data) {
    return $.ajax({
        url: '/ReportGenerator/generate_AJAX',
        async: false,
        data: data,
        success: function () {
            console.log('Success');
        },
        error: function () {
            console.log('error');
        }
    });
}

$('#generate_reports').on('click', function () {
    var id_list = $(".report_id").contents().text();

    var i = 0;
    if (requests.length) {
        makeRequest(id_list, i);
    }
});

function makeRequest(id_list, i) {
    var iPromise = generate_AJAX(id_list[i]);
    if (i < requests.length - 1) {
        iPromise.done(makeRequest(id_list, ++i))
    }
}

// Batch report GENERATE
$(document).ready(function () {
    $('#generate_reports').on('click', function (event) {
        $(".report_id").each(function (index) {
            id = $(this).text();
            var data = {
                report_id: id,
                index: index
            };

            $.ajax({
                url: '/ReportGenerator/generate_AJAX',
                async: false,
                data: data,
                beforeSend: function () {
                    paint_wip(id);
                },
                error: function () {
                    paint_error(id);
                }
            });

        });
    });
});


function paint_error(id) {
    $('#error_div_' + id).text("Error! Not created...");
}

function paint_wip(id) {
    setTimeout(function () {
        location.reload()
    }, 1500);

    // $('#button_' + id).removeClass("btn-error").addClass("btn-warning");
}

// function check_height() {
//     $('.page_content').each(function () {
//         if ($(this).height() > 675) {
//             var mention_items = $(this).find($('.dont_break_inside'));
//             var make_jump = mention_items.last();
//             html_string = make_jump.innerHTML;
//             break_string = '</div></div><div class="page_block"><div class="page_content">';
//             make_jump.clone().insertBefore(make_jump);
//             make_jump.innerHTML.replace(html_string, html_string + break_string);
//         }
//
//         // document.body.innerHTML = document.body.innerHTML.replace('</h1>', '</h1><div id="foo"><div id="bar">')
//     });
// }
