from django.shortcuts import render
from .models import Todo
from django.views.generic import ListView
# Create your views here.




class TodoListView(ListView):
    model = Todo
    context_object_name = 'todos'