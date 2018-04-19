
function connect_listener() {
    $('tbody > tr').on('click', function(event) {
        row_index= event.target.closest('tr').rowIndex
        window.location.replace("/function_management/selected/?function_row="+(row_index-1));

    })

    $('.btn-mais-info').on('click', function(event) {
        $( '.open_info' ).toggleClass( "hide" );
    })

};

function init() {
    console.log('IN INIT')

    $('.ajaxProgress').show();
    $.ajax({
        type: "GET",
        url: "/function_management/getfunctionnames/",
        dataType: "json",
        async: true,
        data: {
            csrfmiddelwaretoken: '{{ csrf_token }}'
        },
        success: function(json) {
            var table=json.table
            $('#table_content').html(table);
//            $('.ajaxProgress').hide();
            connect_listener()
            LoadFunctions()
        }
    });
};



function LoadFunctions() {
    console.log('IN LoadFunctions()')
    $('.ajaxProgress').show();
    $.ajax({
        type: "GET",
        url: "/function_management/getfunctioninfos/",
        dataType: "json",
        async: true,
        data: {
            csrfmiddelwaretoken: '{{ csrf_token }}'
        },
        success: function(json) {
            var table=json.table
            $('#table_content').html(table);
            $('.ajaxProgress').hide();
            connect_listener()
        }
    });
};

init()

