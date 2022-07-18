$(".submit").click(function (e) {
    e.preventDefault();
    // console.log($("#form1"));
    var form = $("#form1").serializeArray()
    form = JSON.stringify(form)
    console.log(JSON.parse(form))
    $.ajax({
      type: "POST",
      url: "user/login",                    ///// URL must be specified  
      data: JSON.parse(form),
      dataType: 'json',
      success: function (response) {
        alert(JSON.stringify(response));

      },
      error: function (ex) {
        alert(ex.responseText);
      }
    });
    return false;
  });