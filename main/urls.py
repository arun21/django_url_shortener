from django.urls import path
from . import views

urlpatterns = [
    path('', views.Make, name="Make new"),
    path('<str:token>', views.Home, name="Home"),
    path('about-app', views.About, name="About Page")
]