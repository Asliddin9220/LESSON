from django.contrib import admin
from django.urls import path, include
from .views import contents
urlpatterns = [
path('',contents, name ='contents'),
]