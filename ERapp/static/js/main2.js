  // table1_remove_file_from_model
function submitForm__uploadfiles(cellId, box, redirectPage,col){
    submitForm__01(cellId, box, redirectPage,col);
}
function submitForm__01(cellId, box, redirectPage,col){
    
    var myForm_id="myForm";
    var csrfToken = $("[name=csrfmiddlewaretoken]").val();
    

    


    var myid1 = document.getElementsByName("myid1")[0].value;
    var col_type1 = document.getElementsByName("col_type1")[0].value;
    var button_edit_data_on_table = document.getElementsByName("button_edit_data_on_table")[0].value;

    var table_firstname = document.getElementsByName("table_firstname_"+cellId)[0].value;
    var table_lastname = document.getElementsByName("table_lastname_"+cellId)[0].value;
    var table_address = document.getElementsByName("table_address_"+cellId)[0].value;
    var table_num = document.getElementsByName("table_num_"+cellId)[0].value;
    var table_email = document.getElementsByName("table_email_"+cellId)[0].value;
    var table_etat = document.getElementsByName("table_etat_"+cellId)[0].value;
    var table_tp = document.getElementsByName("table_tp_"+cellId)[0].value;
    var table_cofrac = document.getElementsByName("table_cofrac_"+cellId)[0].value;
    var table_auditeur = document.getElementsByName("table_auditeur_"+cellId)[0].value;
    
    var table_paiement = document.getElementById("table_paiement_"+cellId);
    if (table_paiement.checked == true){
        var table_paiement_send_state = "True";
    } else {
        var table_paiement_send_state = "False";
    }
   

    // Construct the names of the file input elements
    var table_VT_input_name = 'table_VT_' + cellId;
    var table_auditV1_input_name = 'table_auditV1_' + cellId;
    var table_auditV2_input_name = 'table_auditV2_' + cellId;
    var table_auditV3_input_name = 'table_auditV3_' + cellId;
    var table_auditFinal_input_name = 'table_auditFinal_' + cellId;
    // Get the file input elements using the constructed names
    var table_VT_input = document.querySelector('input[name="' + table_VT_input_name + '"]');
    var table_auditV1_input = document.querySelector('input[name="' + table_auditV1_input_name + '"]');
    var table_auditV2_input = document.querySelector('input[name="' + table_auditV2_input_name + '"]');
    var table_auditV3_input = document.querySelector('input[name="' + table_auditV3_input_name + '"]');
    var table_auditFinal_input = document.querySelector('input[name="' + table_auditFinal_input_name + '"]');


    var formData = new FormData();

    // Append other data to the FormData object
    formData.append('cellId_new', cellId);
    formData.append('table_firstname', table_firstname);
    formData.append('table_lastname', table_lastname);
    formData.append('table_address', table_address);
    formData.append('table_num', table_num);
    formData.append('table_email', table_email);
    formData.append('table_etat', table_etat);
    formData.append('table_tp', table_tp);
    formData.append('table_cofrac', table_cofrac);
    formData.append('table_auditeur', table_auditeur);
    formData.append('table_paiement', table_paiement_send_state);
    formData.append('redirect_page', redirectPage);
    formData.append('myid1', myid1);
    formData.append('col_type1', col_type1);
    formData.append('button_edit_data_on_table', button_edit_data_on_table);
    formData.append('csrfmiddlewaretoken', csrfToken);


    // Append all files from table_VT_input to the FormData object
    for (var i = 0; i < table_VT_input.files.length; i++) {
        formData.append('table_VT[]', table_VT_input.files[i]);
    }

    // Append all files from table_auditV1_input to the FormData object
    for (var i = 0; i < table_auditV1_input.files.length; i++) {
        formData.append('table_auditV1[]', table_auditV1_input.files[i]);
    }

    // Append all files from table_auditV2_input to the FormData object
    for (var i = 0; i < table_auditV2_input.files.length; i++) {
        formData.append('table_auditV2[]', table_auditV2_input.files[i]);
    }
    // Append all files from table_auditV2_input to the FormData object
    for (var i = 0; i < table_auditV3_input.files.length; i++) {
        formData.append('table_auditV3[]', table_auditV3_input.files[i]);
    }
    // Append all files from table_auditV2_input to the FormData object
    for (var i = 0; i < table_auditFinal_input.files.length; i++) {
        formData.append('table_auditFinal[]', table_auditFinal_input.files[i]);
    }

    var loading_spinner_div = `<div class="upload_spinner" id="upload_spinner_1"></div> `  
    $("body").prepend(loading_spinner_div);


    $.ajax({
        url: "/table-view/",
        type: "POST",
        data:  formData,
        processData: false, // Important: tell jQuery not to process the data
        contentType: false, // Important: tell jQuery not to set contentType
        
        success: function(data){
            //window.location.href=table_firstname 
            // update the specific  div {new contant}
            //("#resultDiv").html(data);
            if(data.re_page){
                location.reload();
            }
            table_VT_input.value = null;
            table_auditV1_input.value = null;
            table_auditV2_input.value = null;
            table_auditV3_input.value = null;
            table_auditFinal_input.value=null
            var row = document.getElementById("tr_"+cellId);
            var button_edit_data_on_T = row.querySelector('i');
            if (row) {
                row.style.borderColor = "#0dcaf0";
                button_edit_data_on_T.style.color="green";
 
            }

            
            // Loop through files and prepend new list items
            
            for (var i = 0; i < data.files_date_for_response.length; i++) {
                var F = data.files_date_for_response[i];
                var element_id="#ul_for_"+F.column+"_"+F.file_id;
                var new_File = `

                    <li id="li_for_${F.column}_${F.file_id}" class="color_red_important">
                        <li class="list-inline-item">
                            <a class="nav-link nav-icon show" ><i class=" ${F.I_icon_class} " ></i></a>
                        </li>
                        ${F.file_name}
                        <li class="list-inline-item">
                        <button  class="button_table_data" type="button"  disabled">
                        <i class="ri-delete-bin-2-fill color_gray" style="color:gray;"></i>
                        </button>
                    </li>
                    </li>
                    
                `

                
                $(element_id).prepend(new_File);
                //$("#div_for_vt_DcvWOFJbEf").prepend(new_File);
            }
                
            const remove_loading_spinner_div = document.getElementById("upload_spinner_1");
            remove_loading_spinner_div.remove()
            



        },

    });

}

initializeInput_change('tableDATA_1');
initializeInput_change('tableDATA_2');
initializeInput_change('tableDATA_3');
initializeInput_change('tableDATA_4');
initializeInput_change('tableDATA_5');
initializeInput_change('tableDATA_6');
initializeInput_change('tableDATA_7');
initializeInput_change('tableDATA_8');
initializeInput_change('tableDATA_9');

function initializeInput_change(tableId) {
    document.addEventListener("DOMContentLoaded", function() {
        // Get all input elements within the table
        var inputElements = document.querySelectorAll("#"+tableId+" tbody input[type='text'], #"+tableId+" tbody input[type='file'], #"+tableId+" tbody select ");

        // Store the original values in a data attribute
        inputElements.forEach(function(input) {
            input.dataset.originalValue = input.value;
        });

        // Listen for input changes
        inputElements.forEach(function(input) {
            input.addEventListener("input", function() {
                updateRowColor(input.closest("tr"),tableId);
            });
        });
    });
}
function updateRowColor(row,cellId) {
    // Check if at least one input has a different value from its original value
    var rowShouldBeRed = Array.from(row.querySelectorAll("input[type='text'], input[type='file'],  tbody select ")).some(function(input) {
        return input.value !== input.dataset.originalValue;
    });
    //var button_edit_data_on_T = document.getElementById("i_for_edit_button_"+cellId); //document.getElementsByClassName("i_for_edit_button")[0];
    const button_edit_data_on_T = row.querySelector('i');
    // Set the row color based on the check
    if (rowShouldBeRed) {
        row.style.borderColor = "red";
        button_edit_data_on_T.style.color="red";
    } else {
        row.style.borderColor = "#0dcaf0"; // Reset to the default background color
        button_edit_data_on_T.style.color="green";
    }
}


function remove_file_from_m(id, index, column, redirect_next_page,element_tag_id) {

    var element_tag_id_index=element_tag_id;
    
    var csrfToken = $("[name=csrfmiddlewaretoken]").val();
    
    $.ajax({
        url: "/remove_file_from_MODELS/",
        type: "POST",
        data: {
            param0: id,
            param1:index,
            param2:column,
            param3:redirect_next_page,
            element_tag_id_index:element_tag_id_index,
            csrfmiddlewaretoken: csrfToken
        },
        success: function (response) {
            
             
            var remove_file_from_box_2 = document.getElementById(element_tag_id_index);
            remove_file_from_box_2.style.display="";
            


            //if(data.status =="success"){
            var file_removed_status_box = `
            <div class="file_removed_status_box" id="file_removed_status_box_1">
                <h4>${response.title}</h4>
            </div> `  ;
            $("body").prepend(file_removed_status_box);
            $("#file_removed_status_box_1").delay(2000).fadeOut(200);
            
            //$('#file_removed_status_box_1').remove();
            //}

        },
    });
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
                    
    inpust_msg_col_id="input_msg_"+col+"_" + cellId;
    var message = document.getElementById(inpust_msg_col_id).value;
    var csrfToken = $("[name=csrfmiddlewaretoken]").val();
    
    $.ajax({
        url: "/send-message/",
        type: "POST",
        data: {
            message: message,
            box:box,
            redirectNextPage:redirectNextPage,
            cellId:cellId,
            col:col,
            csrfmiddlewaretoken: csrfToken
        },
        success: function (data) {
            document.getElementById(inpust_msg_col_id).value = ''; // Clear the input field
            var newMessage = `
                <li class="message-item">
                    <a>
                        <img src="${data.userProfilePic}" alt="Image" width="50"class="rounded-circle">
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
            $("#chat-messages-container_"+col+"_"+cellId).prepend(newMessage);

            document.getElementById(inpust_msg_col_id).value = '';

        },
    });

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


