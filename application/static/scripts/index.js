// docSlider Initialization
docSlider.init({
    pager: false
});

// datatables Initialization
$(document).ready( function () {
    $('#rooms').DataTable({
        "bLengthChange" : false,
        language: {
            searchPlaceholder: "Search Room"
        }
    });
} );