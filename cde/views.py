from django.http import HttpResponse
from django.shortcuts import redirect, render
from cde.forms import NewProcessForm,AddCnnForm
from cde.models import NewProcess

# Create your views here.
def index(request):
    newprocessform = NewProcessForm()
    return render(request,"index.html", context={'newprocessform':newprocessform})
def cnn_view(request):
    newprocessform = AddCnnForm()
    return render(request,"cnn.html", context={'form':newprocessform})

def new_process(request):
    form=NewProcessForm()
    if request.method == "POST":
        form = NewProcessForm(request.POST)
        print(form.is_valid())
        if form.is_valid(): 
            form.save()
        
    if request.POST.get('classification_model')=='yes':
        return redirect(cnn_view)
    else:
        return redirect(index)


def add_cnn(request):
  if request.method == "POST":
    form = AddCnnForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = AddCnnForm()
  return redirect(index)