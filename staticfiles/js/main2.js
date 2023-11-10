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



function sendMessage(cellId, box, redirectNextPage,col) {
    inpust_msg_col_id="input_msg_"+col+"_" + cellId
    var message = document.getElementById(inpust_msg_col_id).value;
    
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
                document.getElementById(inpust_msg_col_id).value = ''; // Clear the input field
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
                $("#chat-messages-container_"+col).prepend(newMessage);

                document.getElementById(inpust_msg_col_id).value = '';

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




function sortTable12(table_id, n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById(table_id);
    switching = true;
    // Set the sorting direction to ascending:
    dir = "asc"; 
    /* Make a loop that will continue until
    no switching has been done: */
    while (switching) {
      // Start by saying: no switching is done:
      switching = false;
      rows = table.rows;
      /* Loop through all table rows (except the
      first, which contains table headers): */
      for (i = 1; i < (rows.length - 1); i++) {
        // Start by saying there should be no switching:
        shouldSwitch = false;
        /* Get the two elements you want to compare,
        one from the current row and one from the next: */
        x = rows[i].getElementsByTagName("TD")[n].textContent;
        y = rows[i + 1].getElementsByTagName("TD")[n].textContent;
        /* Check if the two rows should switch place,
        based on the direction, asc or desc: */
        if (dir == "asc") {
          if (x.toLowerCase() > y.toLowerCase()) {
            // If so, mark as a switch and break the loop:
            shouldSwitch = true;
            break;
          }
        } else if (dir == "desc") {
          if (x.toLowerCase() < y.toLowerCase()) {
            // If so, mark as a switch and break the loop:
            shouldSwitch = true;
            break;
          }
        }
      }
      if (shouldSwitch) {
        /* If a switch has been marked, make the switch
        and mark that a switch has been done: */
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
        // Each time a switch is done, increase this count by 1:
        switchcount++;
      } else {
        /* If no switching has been done AND the direction is "asc",
        set the direction to "desc" and run the while loop again. */
        if (switchcount == 0 && dir == "asc") {
          dir = "desc";
          switching = true;
        }
      }
    }
  }

function sortTable(table_id,n,Date_Time_TD) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById(table_id);
    switching = true;
    dir = "asc";

    // Make sure to define the parseDateTime function
    function parseDateTime(dateTimeString) {
        const [day, month, year, time] = dateTimeString.split(' ');
        const [hour, minute] = time.split(':');
        return new Date(year, month - 1, day, hour, minute);
    }

    while (switching) {
        switching = false;
        rows = table.rows;

        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;

                            
            var tdElementx = rows[i].getElementsByTagName("TD")[n];
            var tdElementy = rows[i + 1].getElementsByTagName("TD")[n];
            

            if (tdElementx.querySelector('input') !== null) {
                var inputElementx = tdElementx.querySelector('input');
                var inputValuex = inputElementx.value;

            } else {
                if (tdElementx.querySelector('p') !== null){
                    var inputElementx = tdElementx.querySelector('p');
                    var inputValuex = inputElementx.textContent;
                } else {
                    if (tdElementx.querySelector('select') !== null){
                        var inputElementx = tdElementx.querySelector('select');
                        var inputValuex = inputElementx.value;
                    } else {
                        var inputValuex = tdElementx.textContent;
                    }
                }
            }

            if (tdElementy.querySelector('input') !== null) {
                var inputElementy = tdElementy.querySelector('input');
                var inputValuey = inputElementy.value;

            } else { 
                if (tdElementy.querySelector('p') !== null) {
                    var inputElementy = tdElementy.querySelector('p');
                    var inputValuey = inputElementy.textContent;
                } else {
                    
                    if (tdElementy.querySelector('select') !== null) {
                        var inputElementy = tdElementy.querySelector('select');
                        var inputValuey = inputElementy.value;
                    } else {
                        
                        var inputValuey =  tdElementy.textContent;
                        
                    }
                }
            }

            if (Date_Time_TD){
                var inputValuex = parseDateTime(inputValuex);
                var inputValuey = parseDateTime(inputValuey);

                if (dir == "asc") {
                    if (inputValuex > inputValuey) {
                        shouldSwitch = true;
                        break;
                    }
                } else if (dir == "desc") {
                    if (inputValuex < inputValuey) {
                        shouldSwitch = true;
                        break;
                    }
                }
            }
            else{

                if (dir == "asc") {
                    if (inputValuex.toLowerCase() > inputValuey.toLowerCase()) {
                        shouldSwitch = true;
                        break;
                    }
                } else if (dir == "desc") {
                    if (inputValuex.toLowerCase() < inputValuey.toLowerCase()) {
                        shouldSwitch = true;
                        break;
                    }
                }
            }
            
        }

        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchcount++;
        } else {
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }
}