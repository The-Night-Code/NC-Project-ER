document.getElementById("TAB-1").click();

function myFunction_show_div(div_id){
    var xi = document.getElementById("show_div_i_"+div_id);
    var xdiv = document.getElementById("show_div_"+div_id);
    if (xdiv.style.display === "block") {
      xdiv.style.display = "none";
      xi.classList.add('ri-arrow-down-s-line');

      xi.classList.remove('ri-arrow-up-s-line');
     
    } else {
      xdiv.style.display = "block";
      xi.classList.add('ri-arrow-up-s-line');
      xi.classList.remove('ri-arrow-down-s-line');

    }
  }
var canvas = document.getElementById('signature-canvas');
var signaturePad = new SignaturePad(canvas);

// Clear the signature
document.getElementById('clear-signature').addEventListener('click', function() {
signaturePad.clear();
});

function open_form(evt, tab_name) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tab_content_onclick");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tab_name).style.display = "block";
    evt.currentTarget.className += " active";
  }