from django.urls import path
from . import views

urlpatterns = [
    path('',views.options,name="index"),
    path('choice/',views.computer_choice,name="choice"),
]