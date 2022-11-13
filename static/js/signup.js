$(document).ready(function() {
    console.log("ready")
    $('#id_user_type').change(function() {
        console.log('clicked');
        if ($("#id_user_type :selected").val() == "1"){
            $("[name='athleteInfo']").show();
        }
        else{
            $("[name='athleteInfo']").hide();
        }
      });
  });