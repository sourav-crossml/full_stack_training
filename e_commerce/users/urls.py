from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.Registeruser.as_view())
]
