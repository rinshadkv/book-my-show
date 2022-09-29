$(document).ready(function () {
  


 

  $("#select-date-modal").modal("show")


  $(function () {
    var dtToday = new Date();

    var month = dtToday.getMonth() + 1;
    var day = dtToday.getDate();
    var year = dtToday.getFullYear();
    if (month < 10)
      month = '0' + month.toString();
    if (day < 10)
      day = '0' + day.toString();

    var maxDate = year + '-' + month + '-' + day;



    $('#show-date').attr('min', maxDate);
  });


  $("#continue-btn").click(function () {


    $("#select-date-modal").modal('hide')

    var show_date = $("input[id='show-date']").val();
    var seat_category = $("input[name='seat_category']:checked").val();
    var num_of_seats = $("input[name='number-of-seats']:checked").val();
    var show_time = $("#show-time").val()

    $("input:checkbox").click(function() {
      var n_seats = $("input:checkbox:checked").length ;
      if(n_seats > num_of_seats) {

       
      $("input:checkbox").prop('checked', false)}   

      });

    

    if (seat_category == "premium") {

      $(".standard").css({ "pointer-events": "none", })
      $(".standard-seat").css({ "background-color": "gray" })

      $("#totel_amount").val(totel_amount)
    }
    else {
      $(".premium").css({ "pointer-events": "none", })
      $(".premium-seat").css({ "background-color": "gray" })


    }
    
    $.ajax({
      url: "/check_avilable/",
      type: "GET",
      data: {
        show_date: $("input[id='show-date']").val(),
        seat_category : $("input[name='seat_category']:checked").val(),
        num_of_seats:$("input[name='number-of-seats']:checked").val(),
        show_time:$("#show-time").val()






      },
      success: function (response) {

        if (response.avilable_seats == "yes") {
          alert("room is already booked")
        }
        else {

        }


      }



      }),
       
     
      


      $("#pay-btn").click(function () {

        var selected_seats = [];
        $.each($("input[type='checkbox']:checked"), function () {
          selected_seats.push($(this).val());
        });

      })


  })
  

  
 

})


