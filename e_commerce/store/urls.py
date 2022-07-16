from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryView.as_view()),
    path('product/', views.ProductView.as_view()),
    path('', views.index, name='index'),
    path('login_page', views.login_page, name='login_page')
]
