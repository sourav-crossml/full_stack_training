from django.http import HttpResponse
from django.shortcuts import redirect, render
from cde.forms import NewProcessForm
from cde.models import NewProcess

# Create your views here.
def index(request):
    newprocessform = NewProcessForm()
    return render(request,"index.html", context={'newprocessform':newprocessform})

def new_process(request):
    if request.method == "POST":
        data = NewProcess()
        data.process_name = request.POST.get('process_name')
        data.input_document = request.POST.get('input_document')
        data.pipeline = request.POST.get('pipeline')
        data.classification_model = request.POST.get('classification_model')
        data.time_zone = request.POST.get('time_zone')
        data.process_sla = request.POST.get('process_sla')
        data.pre_processing = request.POST.get('pre_processing')

        data.save()
        return redirect(index)