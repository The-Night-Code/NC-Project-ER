$(document).ready(function () {
    $("#btn-Submit_Upload_image").on("click", function () {
        // Get the selected image file
        var fileInput = $("#my_uploaded_image")[0];
        var file = fileInput.files[0];
        if(file){
            // Create FormData object and append the file
            var formData = new FormData();
            formData.append("my_uploaded_image", file);

            // Make AJAX request
            $.ajax({
                type: "POST",
                url: "/Upload-Profile-Pic/",
                data: formData,
                processData: false,
                contentType: false,
                cache: false,  // Add this line to prevent caching
                success: function (response) {
                if(response.status=="success"){   
                    if(response.refresh_page){   
                        location.reload();
                    }

                }

                if(response.status=="error"){   
                    console.log("error  error  error ");
                }
                },

            });}
    });
});