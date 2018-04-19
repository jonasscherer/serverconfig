function connect_listener() {
    $('tbody > tr').on('click', function(event) {
        row_index= event.target.closest('tr').rowIndex
        window.location.replace("/function_management/deploy/function/?index="+(row_index-1));

    })

}

function redirect(url) {
    window.location.replace(url);
};

function show_table(html_table) {
    $('#table_content').html(html_table);

};