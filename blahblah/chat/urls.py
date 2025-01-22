from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('chats/', views.ChatSessionView.as_view()),
    path('chats/<url>/', views.ChatSessionView.as_view()),
    path('chats/<url>/messages/', views.ChatSessionMessageView.as_view()),
]