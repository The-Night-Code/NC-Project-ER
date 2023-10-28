  // table1_remove_file_from_model
function remove_file_from_m(id, index, column, redirect_next_page) {
    var url = "/remove_file_from_MODELS/?param0=" + encodeURIComponent(id) +
                "&param1=" + encodeURIComponent(index) +
                "&param2=" + encodeURIComponent(column) +
                "&param3=" + encodeURIComponent(redirect_next_page);

    window.location.href = url;
}


document.addEventListener("DOMContentLoaded", function () {
    const toggleIcon = document.getElementById("toggle-dropdown");
    const dropdownMenu = document.querySelector(".dropdown-menu");
  
    toggleIcon.addEventListener("click", function (e) {
      e.preventDefault();
      dropdownMenu.style.display = dropdownMenu.style.display === "block" ? "none" : "block";
    });
});



function sendMessage(cellId, box, redirectNextPage) {
    var message = document.getElementById("input_msg_" + cellId).value;

    if (message !== '') {
        var csrfToken = $("[name=csrfmiddlewaretoken]").val();

        $.ajax({
            url: "/send-message/",
            type: "POST",
            data: {
                message: message,
                box:box,
                redirectNextPage:redirectNextPage,
                cellId:cellId,
                csrfmiddlewaretoken: csrfToken
            },
            success: function (data) {
                document.getElementById("input_msg_" + cellId).value = ''; // Clear the input field
                var newMessage = `
                    <li class="message-item">
                        <a>
                            <img src="${data.userProfilePic}" alt="Image" class="rounded-circle">
                            <div>
                                <h3>${data.username}</h3>
                                <h4>${data.message}</h4>
                                <p> quelques secondes </p>  <!-- Use the naturaltime filter here -->
                            </div>
                        </a>
                    </li>
                    <li>
                        <hr class="dropdown-divider">
                    </li>
                `;

                // Append the new message to the chat box
                $("#chat-messages-container").prepend(newMessage);

                document.getElementById("input_msg_" + cellId).value = '';

            },
        });
    }
}

function preventSubmit(event) {
    if (event.key === "Enter") {
        event.preventDefault(); // Prevent the form submission
    }
}




initializeTable('tableDATA_1');
initializeTable('tableDATA_2');
initializeTable('tableDATA_3');
initializeTable('tableDATA_4');
initializeTable('tableDATA_5');
initializeTable('tableDATA_6');
initializeTable('tableDATA_7');
initializeTable('tableDATA_8');
initializeTable('tableDATA_9');

function initializeTable(tableId) {
    const rows = document.querySelectorAll(`#${tableId} tbody tr`);
    rows.forEach(row => {
        const selectElement = row.querySelector('.form-select');

        // Initial call to set the badge based on the default selected option in each row
        updateBadge(row);

        selectElement.addEventListener('change', () => {
            updateBadge(row);
        });
    });
}


// <select> with <span>badge for tbody
// Function to update the badge based on the selected option in a row
function updateBadge(row) {
    const selectElement = row.querySelector('.form-select');
    const badgeElements = row.querySelectorAll('.badge');
    const selectedOption = selectElement.value;

    badgeElements.forEach(badge => {
        if (badge.getAttribute('data-badge') === selectedOption) {
            badge.style.display = 'inline-block';
        } else {
            badge.style.display = 'none';
        }
    });
}



//<select> with <span>badge for tfoot  
const selectElement = document.querySelector('.form-selectfoot');
const badgeElements = document.querySelectorAll('.badgefoot');

// Function to update the badge based on the selected option
function updateBadgefoot() {
    const selectedOption = selectElement.value;
    badgeElements.forEach(badgefoot => {
        badgefoot.style.display = 'none';
    });
    document.querySelector(`.badgefoot[data-badgefoot="${selectedOption}"]`).style.display = 'inline-block';
}

// Initial call to set the badge based on the default selected option
updateBadgefoot();

// Add event listener to update the badge when the select element changes
selectElement.addEventListener('change', updateBadgefoot);








// Initialize tables with different IDs

// Add more tables as needed

