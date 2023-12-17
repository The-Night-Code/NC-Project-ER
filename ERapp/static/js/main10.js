function add_1_to_i_files_box(iddd) {

    // Get the span element by its ID
    var spanElement = document.getElementById(iddd);
    var currentValue = parseInt(spanElement.innerHTML, 10);
      // Add 1 to the current value
    var newValue = currentValue + 1;
      // Update the span with the new value
    spanElement.innerHTML = newValue;

}