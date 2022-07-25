$(document).ready(function () {
    $("document").ready(function () {
        $.ajax({
            type: "GET",
            url: "product/",
            success: function (response) {
                // console.log(obj, 'response');
                var dynamic = document.querySelector('.row');
                for (let i = 0; i < response.category.length; i++) {
                    var fetch = document.querySelector('.row').innerHTML;
                    dynamic.innerHTML = `
                    <div class="card col-3 m-5" style="width: 18rem;">
                    <img src="`+ response.category[i].image + `" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">`+ response.category[i].name + ` </h5>
                      <h5 class="card-title">`+ response.category[i].price + `Rs. </h5>
                      <p class="card-text">`+ response.category[i].description + `</p>
                      <form method="post" id="form2">
                      <buttton class="card-text aa btn btn-primary" type="button" name="c_id"  value="`+ response.category[i].id + `">Add to cart</buttton>
                      </form>
                    </div>
                   
                  </div>` + fetch;

                }

            },
            error: function (ex) {
                alert(ex.responseText);
            }
        });
        return false;
    })
})


$(document).on("click",".aa",function(e) {
  console.log(e.currentTarget.attributes[3].nodeValue)


  
    e.preventDefault();
    // console.log($("#form1"));
    var form = $("#form2").serializeArray()
    form = JSON.stringify({'product':e.currentTarget.attributes[3].nodeValue})
    console.log(form)
    $.ajax({
      type: "POST",
      url: "cart",                    ///// URL must be specified  
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

// $(document).ready(function () {
//     $("#submitButton").click(function () {
//         $.ajax({
//             type: "GET",
//             url: "filter_obj/",
//             success: function (response) {
//                 debugger
//                 obj = console.log(response.category)
//                 var dynamic = document.querySelector('.row');
//                 for (let i = 0; i < response.category.length; i++) {
//                     var fetch = document.querySelector('.row').innerHTML;
//                     dynamic.innerHTML = `
//                     <div class="card col-3 m-5" style="width: 18rem;">
//                     <img src="`+ response.category[i].image + `" class="card-img-top" alt="...">
//                     <div class="card-body">
//                       <h5 class="card-title">`+ response.category[i].name + ` </h5>
//                       <p class="card-text">`+ response.category[i].description + `</p>
//                       <a href="#" class="btn btn-primary">Go somewhere</a>
//                     </div>
                   
//                   </div>` + fetch;

//                 }

//             },
//             error: function (ex) {
//                 alert(ex.responseText);
//             }
//         });
//         return false;
//     })
// })