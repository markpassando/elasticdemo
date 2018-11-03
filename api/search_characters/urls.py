from django.urls import path
from . import views

urlpatterns = [
  path('getUsers/', views.GetUsers.as_view()),
]