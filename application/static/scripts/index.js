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

window.onload = function(){
	const openRoomSettings = document.querySelector(".pure-button")
    const  closeRoomSettings = document.querySelector(".modal-close")
    const overlay = document.querySelector('#modal-overlay')

    openRoomSettings.onclick = function(){
    	const modal = document.querySelector('#room-settings')
    	modal.classList.add('active')
    	overlay.classList.add('active')

    }

    closeRoomSettings.onclick = function(){
    	const modal = document.querySelector('#room-settings')
    	modal.classList.remove('active')
    	overlay.classList.remove('active')
    }

    overlay.onclick = function(){
    	const modal = document.querySelector('#room-settings')
    	modal.classList.remove('active')
    	overlay.classList.remove('active')
    }
}