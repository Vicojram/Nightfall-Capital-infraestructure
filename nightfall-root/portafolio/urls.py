from django.urls import path
from . import views

urlpatterns = [
    path("", views.portafolio_index, name="portafolio"),
    path("/main_dashboard", views.main_dashboard, name= "main_dashboard"),
]