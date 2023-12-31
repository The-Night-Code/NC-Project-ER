
const chatSocket = new WebSocket("ws://" + window.location.host + "/");

function sendMessage(cellId,numb,redirect_next_page,col){
    var messageInput = document.querySelector("#input_msg_"+col+"_"+cellId).value;
    chatSocket.send(JSON.stringify({ message: messageInput, 
                email : USER_email,
                username : USER_last_name+"  "+USER_first_name,
                userProfilePic:userProfilePic,
                col:col,
                cellId:cellId,
                //new_msg_received:'',
                }));
};
chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    var div = document.createElement("div");
    div.innerHTML = data.email + " : " + data.message;
    document.querySelector("#input_msg_"+data.col+"_"+data.cellId).value = "";
    
    
    var new_msg_re = data.new_msg_received ? "background-color: rgba(28, 97, 107, 0.9); " : "";

    var newMessage = `
        <div class="message-item row_chat_popup chat_popup_content_si" ${new_msg_re} >

            <div class="chat_popup_content_si_header">
                <div class="row_chat_popup">
                    <img src="${data.userProfilePic}" alt="Image" class="rounded-circle">  <!-- alt="image.title"-->
                </div>
                <div class="row_chat_popup">
                    <h3>${data.username}</h3>
                </div>
            </div>
            <div class="column_chat_popup">
            <div class="row_chat_popup">
                <p class="chat_popup_content_para">${data.message}</p>
            </div>
            </div>
            <p class="chat_popup_content_si_timer">quelques secondes</p>
        </div>
        `;
    $("#chat-messages-container_"+data.col+"_"+data.cellId).prepend(newMessage);
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
    for(var i = 0; i < msg_box_ALL.length; i++) {
        var msg_box_si = msg_box_ALL[i].getElementsByTagName('chat_popup_content_si');
        msg_box_si.style.background = "rgba(28, 97, 107, 0.3)";
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