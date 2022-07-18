$(".submit").click(function (e) {
    e.preventDefault();
    // console.log($("#form1"));
    var form = $("#form1").serializeArray()
    form = JSON.stringify(form)

    // form = JSON.stringify(form)
    console.log(JSON.parse(form))
    $.ajax({
        type: "POST",
        url: "user/register",                    ///// URL must be specified  
        data: JSON.parse(form),
        dataType: 'json',
        success: function (response) {
            alert(JSON.stringify(response));
            if (response.status == 200) {
                window.location.href = "/login_page "
            }

        },
        error: function (ex) {
            alert(ex.responseText);
        }
    });
    return false;
});
