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


function Geolocalisation(){
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function(position) {
            var latitude = position.coords.latitude;
            var longitude = position.coords.longitude;
            var altitude = position.coords.altitude;

            document.getElementById("latitude").textContent = latitude;
            document.getElementById("longitude").textContent = longitude;
            document.getElementById("Geolocalisation_div").style.display = "block";
            if (altitude !== null) {
                document.getElementById("altitude").textContent = altitude + " meters";
            } else {
                document.getElementById("altitude").textContent = "";
            }
            
        });
    } else {
        alert("Geolocation is not available in your browser.");
    }
}


    