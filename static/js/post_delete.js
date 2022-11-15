console.log("loaded");

$(() => {
    $('#deletePostInitial').click(function(){
        $("#confirm").show();
    });
  });


  $(() => {
    $('#cancelDelete').click(function(){
        $("#confirm").hide();
    });
  });