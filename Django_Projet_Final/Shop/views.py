from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response, Http404, HttpResponseRedirect

from .models import ShopModel
from .form import ShopAddForm
from .form import BuyForm

# Create your views here.
def index(request):
    return render(request,'Shop/index.html')

def createview(request):
    context ={}
 
    form = ShopAddForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "Shop/create_view.html", context)

def listview(request):

    context = {}
 
    context["dataset"] = ShopModel.objects.all()
         
    return render(request, "Shop/see_view.html", context)

def detail_view(request, id):
    context ={}

    obj = get_object_or_404(ShopModel, id = id)
    
    form = BuyForm()
    form2 = ShopAddForm(request.POST or None, instance = obj)
    context['form'] = form
    if form.is_valid():
        BoughtStock =  (form['User_Buy'].value())
        ActualStock = ShopModel.objects.get(id = id)
        print (ActualStock.Product_Stock)

    return render(request, "Shop/detail_view.html", context)

def updateview(request, id):

    context ={}
 
    obj = get_object_or_404(ShopModel, id = id)
 
    form = ShopAddForm(request.POST or None, instance = obj)
 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+"Shop/"+id)