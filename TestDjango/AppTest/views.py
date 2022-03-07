from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response, Http404, HttpResponseRedirect

from .models import Question
from .form import QuestionForm

def index(request):
    return render(request,'AppTest/index.html')

def createview(request):
    context ={}
 
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "AppTest/create_view.html", context)

def listview(request):

    context = {}
 
    context["dataset"] = Question.objects.all()
         
    return render(request, "AppTest/see_view.html", context)

def detail_view(request, id):
    context ={}

    context["data"] = Question.objects.get(id = id)
         
    return render(request, "AppTest/detail_view.html", context)

def updateview(request, id):

    context ={}
 
    obj = get_object_or_404(Question, id = id)
 
    form = QuestionForm(request.POST or None, instance = obj)
 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+"AppTest/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "AppTest/edit_view.html", context)

def deleteview(request, id):

    context ={}
 
    obj = get_object_or_404(Question, id = id)
 
 
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/"+"AppTest/"+"list/")
 
    return render(request, "AppTest/delete_view.html", context)