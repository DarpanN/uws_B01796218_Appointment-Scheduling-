document.addEventListener("DOMContentLoaded", function () {
    let deleteButtons = document.querySelectorAll(".delete-btn");

    deleteButtons.forEach(function (button) {
        button.addEventListener("click", function (event) {
            let confirmation = confirm("Are you sure you want to delete this?");
            if (!confirmation) {
                event.preventDefault();
            }
        });
    });
});
