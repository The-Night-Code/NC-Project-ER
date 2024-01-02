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


function sendMessage(cellId,numb,redirect_next_page,col){
    var messageInput = document.querySelector("#input_msg_"+col+"_"+cellId).value;
    chatSocket.send(JSON.stringify({ message: messageInput, 
        email : USER_email,
        username : USER_last_name+"  "+USER_first_name,
        userProfilePic:userProfilePic,
        col:col,
        cellId:cellId,

    }));
    
    //var msg_box_ALL = document.getElementById().children;
    var msg_box_ALL = document.getElementById("chat-messages-container_"+col+"_"+cellId);

    for (var i = 0; i < msg_box_ALL.children.length; i++) {
        var msg_box_si = msg_box_ALL.children[i].getElementsByClassName('chat_popup_content_si')[0];

        if (msg_box_si) {
            msg_box_si.style.background = "rgba(28, 97, 107, 0.3)";
        }       
    }
    
};

function OPEN_popUP_chat(id,msg_box,cell_id){
    var divsToHide = document.getElementsByClassName("chat_popup"); //divsToHide is an array
    for(var i = 0; i < divsToHide.length; i++){
        divsToHide[i].style.display = "none"; 
    }
    document.getElementById(id).style.display ="block";

    var csrfToken = $("[name=csrfmiddlewaretoken]").val()
    var chat_span_noti_ID= "chat_span_noti_"+msg_box+"_"+cell_id;

    $.ajax({
        url: "/msg-checker-notif/",
        type: "POST",
        data: {
            id: id,
            chat_span_noti_ID:chat_span_noti_ID,
            msg_box:msg_box,
            cell_id:cell_id,
            csrfmiddlewaretoken: csrfToken,
            processData: false, // Important: tell jQuery not to process the data
            contentType: false, // Important: tell jQuery not to set contentType
        },
        success: function (response) {
            
            
            if(response.status=="success"){   
               
                var spanElement = document.getElementById(response.chat_span_noti_ID);
                  // Update the span with the new value
                spanElement.innerHTML = 0;
                document.getElementById(response.chat_span_noti_ID).classList.remove("OPEN_popUP_chat_span_show");
                document.getElementById(response.chat_span_noti_ID).classList.add("OPEN_popUP_chat_span");
            
            }
            
        },
    });
};

  
 
function CLOSE_popUP_chat(id,msg_box,cell_id) {
    var divsToHide = document.getElementsByClassName("chat_popup"); //divsToHide is an array
    for(var i = 0; i < divsToHide.length; i++){
        divsToHide[i].style.display = "none";
    }
    var msg_si = document.getElementsByClassName("files_popup");

    //var msg_box_ALL = document.getElementById().children;
    var msg_box_ALL = document.getElementById("chat-messages-container_"+msg_box+"_"+cell_id);

    for (var i = 0; i < msg_box_ALL.children.length; i++) {
        //var msg_box_si = msg_box_ALL.children[i].getElementsByClassName('chat_popup_content_si');
        var msg_box_si = msg_box_ALL.children[i].getElementsByClassName('chat_popup_content_si')[0];

        console.log("---- div box"+msg_box_ALL.children.length);
        msg_box_si.style.removeProperty('background-color');
        if (msg_box_si) {
            console.log("plus div box");
            //msg_box_si.style.removeProperty('background-color');
            // Set a new background color
            
        }       
    }

    

};


function OPEN_popUP_files(id){
    var divsToHide = document.getElementsByClassName("files_popup"); //divsToHide is an array
    for(var i = 0; i < divsToHide.length; i++){
        divsToHide[i].style.display = "none"; 
    }
    document.getElementById(id).style.display ="block";
};
  
 
function CLOSE_popUP_files(id) {
    var divsToHide = document.getElementsByClassName("files_popup"); //divsToHide is an array
    for(var i = 0; i < divsToHide.length; i++){
        divsToHide[i].style.display = "none"; 
    }
};

function add_1_to_i_chat_box_noti(iddd){// Get the span element by its ID
    var spanElement = document.getElementById(iddd);
    var currentValue = parseInt(spanElement.innerHTML, 10);
      // Add 1 to the current value
    var newValue = currentValue + 1;
      // Update the span with the new value
    spanElement.innerHTML = newValue;

    document.getElementById(iddd).classList.remove("OPEN_popUP_chat_span");
    document.getElementById(iddd).classList.add("OPEN_popUP_chat_span_show");
}


