
const chatSocket = new WebSocket("ws://" + window.location.host + "/");

function sendMessage(cellId,numb,redirect_next_page,col){
    var messageInput = document.querySelector("#input_msg_"+col+"_"+cellId).value;
    chatSocket.send(JSON.stringify({ message: messageInput, 
                email : USER_email,
                username : USER_last_name+"  "+USER_first_name,
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

};