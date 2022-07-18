$(document).ready(function () {
    $("document").ready(function () {
        $.ajax({
            type: "GET",
            url: "product/",
            success: function (response) {
                obj = console.log(response.category)
                // console.log(obj, 'response');
                var dynamic = document.querySelector('.row');
                for (let i = 0; i < response.category.length; i++) {
                    var fetch = document.querySelector('.row').innerHTML;
                    dynamic.innerHTML = `
                    <div class="card col-3 m-5" style="width: 18rem;">
                    <img src="`+ response.category[i].image + `" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">`+ response.category[i].name + ` </h5>
                      <p class="card-text">`+ response.category[i].description + `</p>
                      <a href="#" class="btn btn-primary">Go somewhere</a>
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

$(document).ready(function () {
    $("#submitButton").click(function () {
        $.ajax({
            type: "GET",
            url: "filter_obj/",
            success: function (response) {
                debugger
                obj = console.log(response.category)
                var dynamic = document.querySelector('.row');
                for (let i = 0; i < response.category.length; i++) {
                    var fetch = document.querySelector('.row').innerHTML;
                    dynamic.innerHTML = `
                    <div class="card col-3 m-5" style="width: 18rem;">
                    <img src="`+ response.category[i].image + `" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">`+ response.category[i].name + ` </h5>
                      <p class="card-text">`+ response.category[i].description + `</p>
                      <a href="#" class="btn btn-primary">Go somewhere</a>
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