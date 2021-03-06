// docSlider Initialization
docSlider.init({
    pager: false
});

// datatables Initialization
$(document).ready(function () {
    $('#rooms').DataTable({
        "bLengthChange": false,
        language: {
            searchPlaceholder: "Search Room"
        }
    });
});

// Modal window
window.onload = function () {
    const openRoomSettings = document.querySelector(".pure-button")
    const closeRoomSettings = document.querySelector(".modal-close")
    const overlay = document.querySelector('#modal-overlay')
    const checkbox = document.querySelector('#private-room-checkbox')
    const password = document.querySelector('#invisible')

    openRoomSettings.onclick = function () {
        const modal = document.querySelector('#room-settings')
        const link_out = document.querySelector("#the_link_two")
        const link_in = document.querySelector('#the_link_one')
        link_in.value = link_out.value
        modal.classList.add('active')
        overlay.classList.add('active')


    }

    closeRoomSettings.onclick = function () {
        const modal = document.querySelector('#room-settings')
        modal.classList.remove('active')
        overlay.classList.remove('active')
    }

    overlay.onclick = function () {
        const modal = document.querySelector('#room-settings')
        modal.classList.remove('active')
        overlay.classList.remove('active')
    }

    checkbox.onclick = function () {
        if (checkbox.checked == true) {
            password.classList.add('active')
        } else {
            password.classList.remove('active')
        }
    }
}