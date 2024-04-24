from django.shortcuts import redirect, render

from .models import todo

# Create your views here.
def todo_list(request):
    Todo=todo.objects.all()
    return render(request,"todo.html", {'todo':Todo})

def add_todo(request):
    return render(request,'addtodo.html')

def createtodo(request):
    if request.method=="POST":
       Title=request.POST.get('title')
       Desc=request.POST.get('desc')
       todo.objects.create(title=Title,desc=Desc)
    return render(request,'addtodo.html')

def complete_todo(request,id):
    Todo=todo.objects.get(id=id)

    Todo.completed=True
    Todo.save()
    print(Todo.completed)

    return redirect('/')

def delete_todo(request,id):
    Todo=todo.objects.get(id=id)
    Todo.delete()
    return redirect('/')

def edit_todo(request,id):
    Todo=todo.objects.get(id=id)
    return render(request,'update_todo.html',{'todo':Todo})

def updatetodo(request,id):
    if request.method=="POST":
       print("updating")
       Todo=todo.objects.get(id=id)
       Todo.title=request.POST.get('title')
       Todo.desc=request.POST.get('desc')
       Todo.save()
    return redirect('/')

