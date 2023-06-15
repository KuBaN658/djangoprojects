from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('done', views.DoneView.as_view()),
    path('', views.FeedBackView.as_view()),
    path('<int:id_feedback>', views.UpdateFeedBackView.as_view()),
    path('list', views.ListFeedBack.as_view()),
    path('detail/<id_feedback>', views.DetailFeedBack.as_view()),
]