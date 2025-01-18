from todo.models import Todo
from .serializers import TodoSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView



class TodoListApiView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



class TodoDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer