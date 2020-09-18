from django.urls import path
from . import views

urlpatterns = [
    path('', views.Make, name="Make new"),
    path('about-app', views.About, name="About Page"),
    path('records', views.Records, name="Records"),
    path('<str:token>', views.Home, name="Home")
]