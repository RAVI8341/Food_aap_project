from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader
# Create your views here.
#creating a view for all the list of items on Home page
def index(request):
    data_item = Item.objects.all()
    context = {
        'data_item':data_item,
    }
    return render(request,'food/index.html',context)

# this view is for details.html for displaying the details about a requested item
def detail(request, item_id):
    item=Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request,'food/detail.html',context)