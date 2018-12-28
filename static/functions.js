function updateCNN(data) {
  // Clear the old content
  $('div#cnn_content').text("");
  $.each(data, function(title, link){
    $('div#cnn_content').append(
      $('<p>').text(title).append(
        $('<hr>').attr("class", "red_line")
      )
    );
  });
}

function updateTwitter(data) {
  // Clear the old content
  $('div#twitter_content').text("");
  $.each(data, function(index, text){
    $('div#twitter_content').append(
      $('<p>').text(text).append(
        $('<hr>').attr("class", "blue_line")
      )
    );
  });
}

function reloadContent(page) {
  // Ensure we're not already in the middle of another loading process
  if (isLoading == 0) {
    isLoading = 1;
    // Add the spinner icon to the calling load button
    var button_path = "button#"+page+"_load.loadButton";
    var spinner_id = page+"_spinner";
    $(button_path).text("");
    $(button_path).append(
      $('<i>'));
    $('i').attr("class", "fa fa-circle-o-notch fa-spin").attr("id", spinner_id);
    var text = document.createTextNode('Reload');
    var elem = document.getElementById(page+"_load");
    elem.appendChild(text);

    // Request the appropriate content from server
    var address = (page==="cnn")? url_cnn : url_twitter;
    jQuery.getJSON(address, function(data) {
      // Successful fetch! Update the appropriate list
      (page==="cnn")? updateCNN(data) : updateTwitter(data);
      // Remove the spinner icon
      $(button_path).text("Reload");
      isLoading = 0;
      isDataLoaded = 1;
    });
  }
  else {
  }
}
