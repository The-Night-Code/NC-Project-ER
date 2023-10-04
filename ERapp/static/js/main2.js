function load()
    {document.getElementById("click_side_bar").click();
    
}





document.addEventListener("DOMContentLoaded", function () {
    const toggleIcon = document.getElementById("toggle-dropdown");
    const dropdownMenu = document.querySelector(".dropdown-menu");
  
    toggleIcon.addEventListener("click", function (e) {
      e.preventDefault();
      dropdownMenu.style.display = dropdownMenu.style.display === "block" ? "none" : "block";
    });
});







// Function to filter table rows
function filterTable(myTable,filterInput) {
    var input, filter, table, tr, td, i, j, txtValue;
    input = document.getElementById(filterInput);
    filter = input.value.toUpperCase();
    table = document.getElementById(myTable);
    tr = table.getElementsByTagName("tr");
  
    for (i = 0; i < tr.length; i++) {
      tr[i].style.display = "none"; // Hide the row by default
      td = tr[i].getElementsByTagName("td");
  
      for (j = 0; j < td.length; j++) {
        var inputElement = td[j].querySelector("input[type='text']");
        var pElement = td[j].querySelector("p");
        
        if (inputElement) {
          txtValue = inputElement.value.toUpperCase();
          if (txtValue.indexOf(filter) > -1) {
            tr[i].style.display = ""; // Show the row if a match is found in any input element
            break; // No need to check other cells in this row
          }
        }
  
        if (pElement) {
          txtValue = pElement.textContent || pElement.innerText;
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = ""; // Show the row if a match is found in any <p> element
            break; // No need to check other cells in this row
          }
        }
      }
    }
  }

  // Add event listeners for each input element
  document.getElementById("filterInput_1").addEventListener("keyup", function () {
    filterTable("myTable_1", "filterInput_1");
  });

  document.getElementById("filterInput_2").addEventListener("keyup", function () {
    filterTable("myTable_2", "filterInput_2");
  });

  document.getElementById("filterInput_3").addEventListener("keyup", function () {
    filterTable("myTable_3", "filterInput_3");
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
