from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('cnn_view', views.cnn_view, name='cnn_view'),
    path('new_process', views.new_process, name='new_process'),
    path('add_cnn', views.add_cnn, name='add_cnn'),
]
