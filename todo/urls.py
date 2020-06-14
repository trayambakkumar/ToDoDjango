from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('addTodo/', views.addTodo, name="addTodo"),
    path('deleteTodo/<int:value>/', views.deleteTodo, name="deleteTodo"),
]