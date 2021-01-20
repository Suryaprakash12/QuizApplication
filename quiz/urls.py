
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index(),name='quiz'),
   # path('',views.welcome()),
    path('saveans/',views.saveans),
]
