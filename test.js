// var checkboxes = document.querySelectorAll('.checkbox');
// console.log(checkboxes)
// document.getElementById('select-all').onclick = function () {
//     var sumval = 0;

//     for (var checkbox of checkboxes) {
//         checkbox.checked = this.checked;
//         if (checkbox.checked == true) {
//             var table = document.getElementById("table");
//             sumVal = 0;

//             for (var i = 1; i < table.rows.length; i++) {
//                 sumVal = sumVal + parseInt(table.rows[i].cells[2].innerHTML);
//             }
//             console.log(sumVal);
//             document.getElementById("selected").innerHTML = "Sum Value = " + sumVal;

//             // console.log(sumVal);
//             // document.getElementById('selected').innerHTML = sumVal;
//         }
//         else {
//             sumval = 0;
//             document.getElementById('selected').innerHTML = sumval;
//         }
//     }}










// $(document).ready(function () {
//     $("#add-row").click(function () {
//         var value = document.getElementById("add-row");
//         var firstname = value.options[value.selectedIndex].text;
//         $(".table tbody tr").last().after(
//             '<tr class="fadetext">' +
//             '<td>' +
//                 '<div class="">' +
//                     '<select class="form-select rounded-0 mb-2 text-muted" id="add-row" aria-label="Default select example">' +
//                         '<option selected disabled>Select Account...</option>' +
//                         '<option value="1-11200-Payroll Cheque Account(AUD)">1-11200-Payroll ChequeAccount(AUD)</option>' +
//                         '<option id="12" value="1-11400-Petty Cash(AUD)">1-11400-Petty Cash(AUD)</option>' +
//                         '<option id="21" value="1-11300-Cash Drawer(AUD)">1-11300-Cash Drawer(AUD)</option>' +
//                         '<option id="3" value="1-11500-Clearing A/c(AUD)">1-11500-Clearing A/c(AUD)</option>' +
//                         '<option id="1" value="1-11800-Undeposited Funds(AUD)">1-11800-Undeposited Funds(AUD</option>' +
//                     '</select>' +

//                 '</div>' +
//                 '</td>' +
//             '<td id="" class="hello"><input class="form-control hello" type="text" placeholder="Default input" aria-label="default input example"></td>' +
//             '<td><input class="form-control hello" type="text" placeholder="Default input" aria-label="default input example"></td>' +
//             '<td><input class="form-contro hellol" type="text" placeholder="Default input" aria-label="default input example"></td>' +
//             '<td><input class="form-control hello" type="text" placeholder="Default input" aria-label="default input example"></td>'+
//         '</tr>'

//         );
//     })
// })






count=0;
$(document).ready(function () {
    $("#add-row").click(function () {
        count++;
        var firstname = $('#add-row :selected').text();
        // var lastname = document.getElementById('lastname').innerHTML;
        var email = $("#email").val();
        $(".table tbody tr").last().before(
            '<tr class="fadetext">' +

            '<td>' + firstname + '</td>' +
            '<td><input  placeholder="Default input" class="form-control'+count+' hello" id ="hello"></td>' +
            '<td><input  placeholder="Default input" class="form-control "></td>' +
            '<td><input  placeholder="Default input" class="form-control "></td>' +
            '<td><input  placeholder="Default input" class="form-control "></td>' +

            '</tr>'
        );
    })
    var table = document.getElementById("mytable");
function getSum(val) {

    var sumVal = 0;
    
    for (var i = 1; i < table.rows.length; i++) {
        sumVal = sumVal + parseInt( val)
        // parseInt(table.rows[i].cells[1].innerHTML);
    }
    document.getElementById("selecte").innerHTML = sumVal;
}

var input = document.getElementsByClassName('hello')

Array.prototype.forEach.call(input, function (el, index) {
    el.addEventListener('click',function(){
        // debugger
    if (el.value) {
        getSum(el.value)
    }
    else{
        console.log('enter value')
    }
    })
    
})
})



//     if(table){
//     table.addEventListener('click',function(){
//      debugger
// if(table.rows[1].cells[1].innerHTML != ''){
//         console.log('enter value')
//     }
//     else{
//         getSum()
//     }

//     })
// }
