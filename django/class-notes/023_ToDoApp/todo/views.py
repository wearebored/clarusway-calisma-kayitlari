from django.shortcuts import render,redirect
from django.urls import reverse_lazy
# Create your views here.
from .models import *
from .forms import *
from django.contrib import messages
from django.views.generic import(
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

class TodoListView(ListView):
    model=Todo

class TodoCreateView(CreateView):
    model=Todo
    form_class=TodoForm
    success_url=reverse_lazy('todo_list')
    
class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')
    
class TodoDeleteView(DeleteView):
    model=Todo
    success_url = reverse_lazy('todo_list')

class TodoDetailView(DetailView):
    model = Todo
        
#  Not ! isterseniz class larda
#    template_name = 'todo/todo_delete.html'
#    ile django nun isteği dışına çıkabilirsiniz