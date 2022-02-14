from django.shortcuts import render,redirect
from .models import Lists, Jobs
from django.contrib import messages

# Create your views here.


def home(request):
    list = Lists.objects.all()
    return render(request, 'home.html', {'list': list})


def clist(request):
    if request.method == 'POST':
        list = Lists()
        id = request.POST.get('id')
        title = request.POST.get('name')
        if Lists.objects.filter(title=title):
            messages.info(request, 'List already exists')
            return redirect('/')
        elif title == "":
            messages.info(request, 'List Name Cannot be Blank')
        else:
            list.title = title
            list.save()
            messages.info(request, 'List Created')
            return redirect('/')
    return redirect('/')


def list(request, pk):
    listx = Lists.objects.get(id=pk)
    listy = Lists.objects.all()
    job = Jobs.objects.all()
    return render(request, 'lists.html', {'listx': listx, 'jobs': job, 'listy': listy})


def job(request):
    jo = Jobs()
    title = request.GET.get('title')
    description = request.GET.get('description')
    task = request.GET.get('name')
    id = request.GET.get('id')
    if task == "":
        messages.info(request, 'Task Cannot Be Blank')
        return redirect('/lists/' + id)
    else:
        jo.title = title
        jo.job = task
        jo.description = description
        jo.save()
        messages.info(request, 'Task added')
        return redirect('/lists/'+id)


def delete(request, sk, pk):
    task = Jobs.objects.get(id=pk)
    task.delete()
    messages.info(request, 'Task Deleted')
    return redirect('/lists/'+sk)


def dellist(request, pk):
    list = Lists.objects.get(id=pk)
    for x in Jobs.objects.all():
        if x.title == list.title:
            x.delete()
    list.delete()
    messages.info(request, 'List Deleted')
    return redirect('/')


def comp(request, sk, pk):
    task = Jobs.objects.get(id=pk)
    task.comp = "true"
    task.save()
    messages.info(request, 'Task Moved To Completed Tasks')
    return redirect('/lists/'+sk)
