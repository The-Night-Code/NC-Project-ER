// Include SignaturePad library
var canvas = document.getElementById('signature-pad');
var signaturePad = new SignaturePad(canvas);

var saveButton = document.getElementById('save-signature');
var savedSignature = document.getElementById('saved-signature');

saveButton.addEventListener('click', function() {

    window.location.href ="dsasdad"
    // Convert the signature to a data URL (base64 image)
    var signatureDataURL = signaturePad.toDataURL();

    // Send the data URL to the server using an AJAX request
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/save_signature/', true);
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    xhr.send(JSON.stringify({ signature: signatureDataURL }));

    xhr.onreadystatechange = function() {

        window.location.href ="as"
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Show the saved signature image
            savedSignature.src = signatureDataURL;
            savedSignature.style.display = 'block';
            // You can also reset the signature pad
            signaturePad.clear();
        }
    };
});
