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
  