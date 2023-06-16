from django.urls import path
from . import views

urlpatterns = [
    path('load_image', views.CreateGalleryView.as_view()),
]