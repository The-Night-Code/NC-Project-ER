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
