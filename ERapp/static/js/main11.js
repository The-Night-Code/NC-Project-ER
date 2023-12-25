
const chatSocket = new WebSocket("ws://" + window.location.host + "/");

function sendMessage(cellId,numb,redirect_next_page,col){
    var messageInput = document.querySelector("#input_msg_"+col+"_"+cellId).value;
    chatSocket.send(JSON.stringify({ message: messageInput, 
                email : USER_email,
                username : USER_last_name+"  "+USER_first_name,
                userProfilePic:userProfilePic,
                col:col,
                cellId:cellId,

                }));
};
chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    var div = document.createElement("div");
    div.innerHTML = data.email + " : " + data.message;
    document.querySelector("#input_msg_"+data.col+"_"+data.cellId).value = "";
    var newMessage = `

        
        
        
        <div class="message-item row_chat_popup chat_popup_content_si">

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

    // Append the new message to the chat box
    $("#chat-messages-container_"+data.col+"_"+data.cellId).prepend(newMessage);
    
// The event listener will log: null

};

function OPEN_popUP_chat(id){


    
    
      
    
    const div_popUP_chat = document.querySelector('.chat_popup');

    var divsToHide = document.getElementsByClassName("chat_popup"); //divsToHide is an array
    for(var i = 0; i < divsToHide.length; i++){
        //divsToHide[i].style.visibility = "hidden"; // or
        divsToHide[i].style.display = "none"; // depending on what you're doing
    }

    document.getElementById(id).style.display ="block";
    //document.getElementById(id).style.display = ;



  }
  

  
function CLOSE_popUP_chat(id) {
    //document.querySelector('.chat_popup').style.display ="none";

    var divsToHide = document.getElementsByClassName("chat_popup"); //divsToHide is an array
    for(var i = 0; i < divsToHide.length; i++){
        //divsToHide[i].style.visibility = "hidden"; // or
        divsToHide[i].style.display = "none"; // depending on what you're doing
    }
//document.getElementById(id).classList.remove("chat_popup_show");
//document.getElementById(id).classList.add("chat_popup_hide");
}