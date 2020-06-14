from django.shortcuts import render, redirect
from .models import TodoItem


# Create your views here.


def index(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'index.html', {'all_items': all_todo_items})


def addTodo(request):
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return redirect('/todo/')


def deleteTodo(request, value):
    item_to_delete = TodoItem.objects.get(id=value)
    item_to_delete.delete()
    return redirect('/todo/')

