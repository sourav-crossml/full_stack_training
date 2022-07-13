from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.Registeruser.as_view()),
    path('login/', views.login_user,name='login')
]
