from django.urls import path
from . import views
urlpatterns = [
    path('category/', views.CategoryView.as_view()),
    path('product/', views.ProductView.as_view()),
    path('index', views.index, name='index')
]
