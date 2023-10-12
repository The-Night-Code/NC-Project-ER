function upload_image_formK_click_button(inp){

    // Set the values of the hidden input fields in the form
    document.getElementById("input_value").value = inp;

    // Check if the input file is not empty
    const fileInput = document.getElementsByName(inp)[0];
    if (fileInput && fileInput.files.length > 0) {
        // If not empty, click the "mybutton1"
        document.getElementById("mybutton1").click();
    } 

  }