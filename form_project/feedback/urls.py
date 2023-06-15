from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('done', views.done),
    path('', views.index),
    path('<int:id_feedback>', views.update_feedback),
]