// task 1
var checkboxes = document.querySelectorAll('.checkbox1');
console.log(checkboxes)


sumVal1 = 0;
sumVal2 = 0;
checkboxes.forEach((check, index) => {
    check.addEventListener('click', function () {

        if (this.checked == true) {

            var table = document.getElementById("table1");
            sumVal1 = sumVal1 + parseInt(table.rows[index + 1].cells[2].innerHTML);
            sumVal2 = sumVal2 + parseInt(table.rows[index + 1].cells[3].innerHTML);
            first()
        }
        else if (this.checked != true) {
            var table = document.getElementById("table1");
            sumVal1 = sumVal1 - parseInt(table.rows[index + 1].cells[2].innerHTML);
            sumVal2 = sumVal2 - parseInt(table.rows[index + 1].cells[3].innerHTML);
            first()
        }
        else {
            sumval1 = 0;
            sumval2 = 0;
            document.getElementById('selected').innerHTML = sumval;
        }
    })
})


var checkboxes = document.querySelectorAll('.checkbox2');
console.log(checkboxes)


sumVal3 = 0;
sumVal4 = 0;
checkboxes.forEach((check, index) => {
    check.addEventListener('click', function () {
        if (this.checked == true) {

            var table = document.getElementById("table2");
            sumVal3 = sumVal3 + parseInt(table.rows[index + 1].cells[2].innerHTML);
            sumVal4 = sumVal4 + parseInt(table.rows[index + 1].cells[3].innerHTML);
            first()
        }
        else if (this.checked != true) {
            var table = document.getElementById("table2");
            sumVal3 = sumVal3 - parseInt(table.rows[index + 1].cells[2].innerHTML);
            sumVal4 = sumVal4 - parseInt(table.rows[index + 1].cells[3].innerHTML);
            first()
        }
        else {
            sumVal2 = 0;
            document.getElementById('selected').innerHTML = sumval2;
        }
    })
})

function first() {
    a = sumVal1 - sumVal3;
    b = sumVal2 - sumVal4
    document.getElementById('selected').innerHTML = a;
    document.getElementById('selected2').innerHTML = b;
}





// task 2





count = 0;
const count_list = []
function my() {
    a = count++;
    count_list.push(a);
    DEBIT = document.createElement('input');
    DEBIT.setAttribute("type", 'text');
    DEBIT.setAttribute("class", 'text');
    DEBIT.setAttribute("id", +count + 'debit');
    DEBIT.setAttribute("onkeypress", 'myFunction1(event)');


    CREDIT = document.createElement('input');
    CREDIT.setAttribute("type", 'text');
    CREDIT.setAttribute("id", +count + 'credit');
    CREDIT.setAttribute("onkeypress", 'myFunction2(event)');


    var slect = document.getElementById("add-row");
    option = slect.options[slect.selectedIndex].value;

    var tbodyRef = document.getElementById('mytable');

    // Insert a row at the end of table
    var newRow = tbodyRef.insertRow(1);

    // Insert a cell at the end of the row
    var newCell = newRow.insertCell(0);
    var newCell1 = newRow.insertCell(1).appendChild(DEBIT);
    var newCell2 = newRow.insertCell(2).appendChild(CREDIT);
    var newCell3 = newRow.insertCell(3);
    var newCell4 = newRow.insertCell(4);

    newCell.innerHTML = option;

}


function myFunction1(event) {
    for (i in count_list) {

        a = event.currentTarget.id;
        b = event.currentTarget.innerHTML;

        console.log(b)
        let result = a.slice(0, 1);
        i++


        if (i == result & b == "") {
            const ds = document.getElementById(+i + "credit")
            ds.disabled = true;
        }
        else if (b != '') {
            const ds = document.getElementById(+i + "credit")
            ds.disabled = false;
        }

    }
}


function myFunction2(event) {
    console.log(this)
    for (i in count_list) {

        a = event.currentTarget.id;
        let result = a.slice(0, 1);
        i++

        if (i == result) {
            const ds = document.getElementById(+i + "debit")
            console.log(ds)
            ds.disabled = true;
        }

    }
}
