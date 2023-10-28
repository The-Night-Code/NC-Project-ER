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



function send_message_box(cell_id,box,redirect_next_page) {
    
    
    var message = document.getElementById("input_msg_"+cell_id).value;
    
    var x1 = document.getElementById("user_email").value;
    var x2 = document.getElementById("user_firstname").value;
    var x3 = document.getElementById("user_lastname").value;
    if (message !== null) {
      var url = "/formT5/?param0="+ encodeURIComponent(cell_id) +
        "&param1=" + encodeURIComponent(x1) +
        "&param2=" + encodeURIComponent(x2) +
        "&param3=" + encodeURIComponent(x3) +
        "&param4=" + encodeURIComponent(box) +
        "&param5=" + encodeURIComponent(message)+
        "&param6="+redirect_next_page;
      window.location.href = url;
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

