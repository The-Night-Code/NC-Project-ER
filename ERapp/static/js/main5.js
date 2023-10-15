
var input1 = document.getElementById("input_msg_112");
input1.addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    window.location.href = "url2";
    event.preventDefault();
    
    document.getElementById("send_msg_1").click();
    
  }
})





