$(() => {
    $('#edit-profile').click(function(){
     $('#edit-profile-modal').addClass('is-active');
    });
    $('.modal-card-head button.delete, .modal-save, .modal-cancel').click(function(){
      $('#edit-profile-modal').removeClass('is-active');
    });
  });
  

  $(() => {
    $('#profilePhoto').click(function(){
     $('#edit-profile-photo').addClass('is-active');
    });
    $('.modal-card-head button.delete, .modal-save, .modal-cancel').click(function(){
      $('#edit-profile-photo').removeClass('is-active');
    });
  });

  function copyEmail(id) {
    // Get the text field
    var copyText = document.getElementById(id).innerText;
  
    // Select the text field
    copyText.select();
    copyText.setSelectionRange(0, 99999); // For mobile devices
  
     // Copy the text inside the text field
    navigator.clipboard.writeText(copyText.value);
  
    // Alert the copied text
    alert("Copied the text: " + copyText.value);
  }
  

  $(() => {
    $('#myDetailBar').click(function(){
     $('#myDetailBar').addClass('is-active');
     $('#myPostBar').removeClass('is-active');
     $("#myDetailContent").show();
     $("[name='myPostContent']").hide();
    });
  });

  $(() => {
    $('#myPostBar').click(function(){
     $('#myPostBar').addClass('is-active');
     $('#myDetailBar').removeClass('is-active');
     $("#myDetailContent").hide();
     $("[name='myPostContent']").show();
    });
  });