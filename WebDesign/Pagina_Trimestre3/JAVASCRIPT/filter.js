// Filter with Bootstrap: https://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_filters_list&stacked=h
$(document).ready(function(){
    $("#myInput").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#myList li").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });