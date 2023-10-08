
var input1 = document.getElementById("input_msg_1");
input1.addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    window.location.href = "url2";
    event.preventDefault();
    
    document.getElementById("send_msg_1").click();
    
  }
});



function send_message_box(cell_id,box) {
                    
    var x0 = document.getElementById("input_msg_1").value;

      var url2="{% url '' %}?"+
        "param=" + encodeURIComponent(x0) +
        "&param0=" + x0 ;
      window.location.href = "url2";

};