from django.shortcuts import render
from .models import Todo
from django.views.generic import ListView , DetailView , CreateView
from .forms import TodoForm
# Create your views here.




class TodoListView(ListView):
    model = Todo
    context_object_name = 'todos'
    template_name = 'todo_list.html'


class TodoDetial(DetailView):
    model = Todo
    context_object_name = 'todo'
    template_name = 'todo_detail.html'


class TodoCreate(CreateView):
    form_class = TodoForm
    template_name = 'todo_create.html'    
    success_url = '/'