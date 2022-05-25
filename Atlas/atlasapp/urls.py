from . import views
from django.urls import path

# urls of app
urlpatterns = [
    path('', views.index, name='index'),
    path('datatable', views.datatable,name='datatable'),
]
