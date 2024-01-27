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

$(document).ready(function () {
    $("#btn-Change_Password").on("click", function () {
        // Get the selected image file
        var csrfToken = $("[name=csrfmiddlewaretoken]").val();
        var newPassword = $("#newPassword").val(); //document.getElementById("newPassword");
        var renewPassword =$("#renewPassword").val(); // document.getElementById("renewPassword");
        console.log("newPassword"+newPassword);
        console.log("renewPassword"+renewPassword);

        // Create FormData object and append the file
        var formData = new FormData();
        formData.append("newPassword", newPassword);
        formData.append("renewPassword", renewPassword);

        formData.append('csrfmiddlewaretoken', csrfToken);
        // Make AJAX request
        $.ajax({
            type: "POST",
            url: "/Change-Password/",
            data: formData,
            processData: false,
            contentType: false,
            cache: false,  // Add this line to prevent caching
            success: function (response) {
            if(response.status=="success"){   
                if(response.refresh_page){   
                    console.log("password changed");

                }

            }

            if(response.status=="error"){   
                console.log("error  at {password changed} ");
            }
            },

        });
    });
});


$(document).ready(function () {
    $("#btn-Remove_Upload_image").on("click", function () {
        // Get the selected image file
        var csrfToken = $("[name=csrfmiddlewaretoken]").val();
        var newPassword = $("#newPassword").val(); //document.getElementById("newPassword");
        var renewPassword =$("#renewPassword").val(); // document.getElementById("renewPassword");
        console.log("newPassword"+newPassword);
        console.log("renewPassword"+renewPassword);

        // Create FormData object and append the file
        var formData = new FormData();
        formData.append("newPassword", newPassword);
        formData.append("renewPassword", renewPassword);

        formData.append('csrfmiddlewaretoken', csrfToken);
        // Make AJAX request
        $.ajax({
            type: "POST",
            url: "/Remove-Profile-Pic/",
            data: formData,
            processData: false,
            contentType: false,
            cache: false,  // Add this line to prevent caching
            success: function (response) {
            if(response.status=="success"){   
                if(response.refresh_page){   
                    console.log("password changed");
                    location.reload();
                }

            }

            if(response.status=="error"){   
                console.log("error  at {password changed} ");
                console.log(response.info);
            }
            },

        });
    });
});