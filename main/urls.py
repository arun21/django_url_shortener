from django.urls import path
from . import views

urlpatterns = [
    path('', views.Make, name="Make new"),
    path('about', views.About, name="About Page")
]