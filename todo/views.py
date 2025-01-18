from django.shortcuts import render
from .models import Todo
from django.views.generic import ListView , DetailView
# Create your views here.




class TodoListView(ListView):
    model = Todo
    context_object_name = 'todos'
    template_name = 'todo_list.html'


class TodoDetial(DetailView):
    model = Todo
    context_object_name = 'todo'
    template_name = 'todo_detail.html'