function displayDivDemo(id, elementValue) {
    document.getElementById(id).style.display = elementValue.value == 1 ? 'block' : 'none';
}

$(document).ready(function () {
    $('#myTable').DataTable();
});

function myFunction(x) {
    console.log("hello")
    alert("Row index is: "+x.text);
}