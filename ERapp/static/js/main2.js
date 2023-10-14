


document.addEventListener("DOMContentLoaded", function () {
    const toggleIcon = document.getElementById("toggle-dropdown");
    const dropdownMenu = document.querySelector(".dropdown-menu");
  
    toggleIcon.addEventListener("click", function (e) {
      e.preventDefault();
      dropdownMenu.style.display = dropdownMenu.style.display === "block" ? "none" : "block";
    });
});














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

// Add event listener for each row in tableDATA1
const rows1 = document.querySelectorAll('#tableDATA_1 tbody tr');

rows1.forEach(row => {
    const selectElement = row.querySelector('.form-select');

    // Initial call to set the badge based on the default selected option in each row
    updateBadge(row);

    selectElement.addEventListener('change', () => {
        updateBadge(row);
    });
});

// Add event listener for each row in tableDATA2
const rows2 = document.querySelectorAll('#tableDATA_2 tbody tr');

rows2.forEach(row => {
    const selectElement = row.querySelector('.form-select');

    // Initial call to set the badge based on the default selected option in each row
    updateBadge(row);

    selectElement.addEventListener('change', () => {
        updateBadge(row);
    });
});

// Add event listener for each row in tableDATA3
const rows3 = document.querySelectorAll('#tableDATA_3 tbody tr');

rows3.forEach(row => {
    const selectElement = row.querySelector('.form-select');

    // Initial call to set the badge based on the default selected option in each row
    updateBadge(row);

    selectElement.addEventListener('change', () => {
        updateBadge(row);
    });
});

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
