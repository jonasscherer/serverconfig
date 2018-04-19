$(function () {
    
    
    $('tbody > tr').on('click', function(event) {
        row_index= event.target.closest('tr').rowIndex 
        $("#row_index").val( row_index );
        var order_object = "{{order_list}}";
        alert(order_object)
        $("#modal_author").val( order_object[row_index].author );
        // As pointed out in comments, 
        // it is superfluous to have to manually call the modal.
        // $('#addBookDialog').modal('show');
        event.preventDefault();

        $('#myModal').modal('show');
    })
    
    $('.btn-mais-info').on('click', function(event) {
        $( '.open_info' ).toggleClass( "hide" );
    })
    
     
});
