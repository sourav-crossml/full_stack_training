from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryView.as_view()),
    path('product/', views.ProductView.as_view()),
    path('', views.index, name='index'),
    path('cart', views.CartView.as_view(), name='cart'),
    path('login_page', views.login_page, name='login_page'),
    path('signup_page', views.signup_page, name='signup_page')
]
