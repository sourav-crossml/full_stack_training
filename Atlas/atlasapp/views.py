from django.shortcuts import render

#home page
def index(request):
    return render(request,"home.html")


# datatables
def datatable(request):
    return render(request,"datatable.html")