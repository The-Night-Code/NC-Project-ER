
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