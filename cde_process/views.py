from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import NewProcessForm, AddCnnForm ,ManageAttributeForm
from .models import NewProcess, AddCnn ,ManageAttribute
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    newprocessform = NewProcessForm()
    return render(request, "index.html", context={'newprocessform': newprocessform})


def cnn_view(request, ):
    add_cnn = AddCnnForm()
    table_values = AddCnn.objects.all()
    return render(request, "cnn.html", context={'form': add_cnn, 'data': table_values})


def mamange_attribute_view(request, ):
    add_cnn = ManageAttributeForm()
    table_values = ManageAttribute.objects.all()
    return render(request, "manage_attribute.html", context={'form': add_cnn, 'data': table_values})


def new_process(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if password==confirmpassword:
            user = User.objects.create_user(first_name=firstname, last_name=lastname,username=username,password=password)
            form = NewProcessForm()
            if request.method == "POST":
                form = NewProcessForm(request.POST)
                if form.is_valid():
                        form.save()
        else:
            return redirect(index)

    if request.POST.get('classification_model') == 'yes':
        add_cnn = AddCnnForm()
        table_values = AddCnn.objects.all()
        return render(request, "cnn.html", context={'form': add_cnn, 'data': table_values})

        # return redirect(cnn_view,{'user':user})
    else:
        return redirect(index)


def add_cnn(request):
    form = AddCnnForm()
    if request.method == "POST" and request.FILES['sample_file']:
        form = AddCnnForm(request.POST)
        if form.is_valid():
            my_model = form.save(commit=False)
            my_model.sample_file = request.FILES['sample_file']
            my_model.save()
    else:
        form = AddCnnForm()
    return redirect(cnn_view)


#   def add_cnn_model(request):
#     form=Cnn_modelForm()
#     print(request.FILES['sample_file'])
#     if request.method == "POST" and request.FILES['sample_file']:
#         form = Cnn_modelForm(request.POST)
#         # breakpoint()
#         if form.is_valid():

#             my_model = form.save(commit=False)
#             my_model.sample_file = request.FILES['sample_file']
#             my_model.cnnclass = "Single_Class value"
#             my_model.save()
