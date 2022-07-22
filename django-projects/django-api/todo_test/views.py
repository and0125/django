from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

class ListTodo(generics.ListAPIView):
    query_set = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.ListAPIView):
    query_set = Todo.objects.all()
    serializer_class = TodoSerializer