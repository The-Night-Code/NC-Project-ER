function add_1_to_i_files_box(iddd) {

    // Get the span element by its ID
    var spanElement = document.getElementById(iddd);
    var currentValue = parseInt(spanElement.innerHTML, 10);
      // Add 1 to the current value
    var newValue = currentValue + 1;
      // Update the span with the new value
    spanElement.innerHTML = newValue;

    document.getElementById(iddd).classList.remove("table_span_calc_files");
    document.getElementById(iddd).classList.add("table_span_calc_files_show");
}


function sendMessage43(cellId, box, redirectNextPage,col) {

  var csrfToken = $("[name=csrfmiddlewaretoken]").val();
  
  $.ajax({
      url: "/send-message/",
      type: "GET",
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
