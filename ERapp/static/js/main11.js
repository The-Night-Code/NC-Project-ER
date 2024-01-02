const chatSocket = new WebSocket("ws://" + window.location.host + "/ws/chat/");

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    var div = document.createElement("div");
    div.innerHTML = data.email + " : " + data.message;
    var bg_color_recieved_msg='';
    if(USER_email != data.email){
        bg_color_recieved_msg='style="background-color:#1C616BE6;"';

        var iddd = "chat_span_noti_"+data.col+"_"+data.cellId;
        var spanElement = document.getElementById(iddd);
        var currentValue = parseInt(spanElement.innerHTML, 10);
          // Add 1 to the current value
        var newValue = currentValue + 1;
          // Update the span with the new value
        spanElement.innerHTML = newValue;
    
        document.getElementById(iddd).classList.remove("OPEN_popUP_chat_span");
        document.getElementById(iddd).classList.add("OPEN_popUP_chat_span_show");

    }
    document.querySelector("#input_msg_"+data.col+"_"+data.cellId).value = "";
    var newMessage = `
        <div class="message-item row_chat_popup chat_popup_content_si" ${bg_color_recieved_msg}>

            <div class="chat_popup_content_si_header" >
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

