from django.urls import path
from . import views


urlpatterns = [
    path('' , views.TodoListView.as_view() , name='todo-list'),
    path('todo-detail/<int:pk>/' ,  views.TodoDetial.as_view() , name='todo-detial'),
    path('todo-create/' , views.TodoCreate.as_view() , name='todo-create'),
    path('todo-update/<int:pk>/' , views.TodoUpdate.as_view() , name='todo-update')
]