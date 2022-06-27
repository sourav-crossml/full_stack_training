from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import NewProcessForm, AddCnnForm
from .models import NewProcess, AddCnn
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    newprocessform = NewProcessForm()
    return render(request, "index.html", context={'newprocessform': newprocessform})


def cnn_view(request, user):
    print(user)
    add_cnn = AddCnnForm()
    table_values = AddCnn.objects.all()
    return render(request, "cnn.html", context={'form': add_cnn, 'data': table_values})


def new_process(request):
    form = NewProcessForm()
    if request.method == "POST":
        form = NewProcessForm(request.POST)
        if form.is_valid():
            form.save()
            userName = request.REQUEST.get('username', None)
            userPass = request.REQUEST.get('password', None)
            userMail = request.REQUEST.get('email', None)
            if userName and userPass and userMail:
                u,created = User.objects.get_or_create(userName, userMail)
        

    if request.POST.get('classification_model') == 'yes':
        user = request.POST.get('process_name')
        id=form.object.only('id').get(name='process_name').id
        print(id)
        add_cnn = AddCnnForm()
        table_values = AddCnn.objects.all()
        return render(request, "cnn.html", context={'form': add_cnn, 'data': table_values,'user':user})

        # return redirect(cnn_view,{'user':user})
    else:
        return redirect(index)


def add_cnn(request):
    form = AddCnnForm()
    if request.method == "POST" and request.FILES['sample_file']:
        form = AddCnnForm(request.POST)
        if form.is_valid():
            my_model =form.save(commit=False)
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