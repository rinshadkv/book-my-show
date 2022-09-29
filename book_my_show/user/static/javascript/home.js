$(document).ready(function(){
  
  $("#change-to-signup").click(function(){
    $("#login-popup").attr({"hidden":true})
    $("#signup-popup").attr({"hidden":false})
  })
    $('#signup-form').validate({
      rules: {
        signup_email: {
          email: true

        },
        password: {
          minlength: 8,
          maxlength: 16

        },
        repassword: {
          equalTo: "#password"

        },
        name: {
          maxlength: 15,
          minlength: 4,
        }
      }

    })
    
    $('#email-signup').change(function(){

      
      $.ajax({
        url:"/check_email/",
        type:"GET",
        data:{
         email: $('#email-signup').val()
        },
        success:function(response){
          if (response.exists==true){
            alert("email alraedy taken")
            $("#email-signup").css({"border-color":"red"})
           


          }
          else{
            $("#email-signup").css({"border-color":"green"})

          }


        }
        

      })














  })})

  // $('#login-btn').click(function () {
  //   $.ajax({
  //     url: 'login',
  //     type: 'GET',
  //     data: {
  //       password:$("#password").val(),

  //       email: $('#email').val(),

  //     },
  //     success: function (response) {
  //       if (response.msg == true) {

  //         alert(' successfully login')

      
  //       }
  //       else {
  //         alert(' something wrong')
  //       }
  //     }
  //   })
  // })



