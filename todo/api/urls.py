from django.urls import path
from . import views

urlpatterns = [
    path('todo/' , views.TodoListApiView.as_view()),
    path('todo/<int:pk>/' , views.TodoDetailApiView.as_view())
]