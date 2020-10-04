from django.shortcuts import render
from .models import todolist

def index(request):
    todo_items=todolist.objects.order_by('id')
    context={'todo_items':todo_items}
    return render(request,'todolist/index.html',context)
    
