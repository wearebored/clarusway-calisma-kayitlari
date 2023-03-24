from django.shortcuts import render,redirect
# Create your views here.
from .models import *
from .forms import *
from django.contrib import messages

def todo_list(request):
    todos=Todo.objects.all()
    context={
        "todos":todos
    }
    return render(request,'list.html',context)
def todo_add(request):
    form=TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Successed')
        return redirect('todo_list')

    return render(request,'add.html',{'form':form})

def todo_update(request,pk):
    todo=Todo.objects.get(id=pk)
    form=TodoForm(instance=todo)
    if request.method=="POST":
        form=TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
        return redirect('todo_list')

    return render(request,'update.html',{'form':form,'todo':todo})

def todo_delete(request,pk):
    todo=Todo.objects.get(id=pk)
    todo.delete()
    return redirect('todo_list')

