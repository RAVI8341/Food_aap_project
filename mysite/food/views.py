from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
#creating a view for all the list of items on Home page
"""def index(request): #function based view
    data_item = Item.objects.all()
    context = {
        'data_item':data_item,
    }
    return render(request,'food/index.html',context)"""
class IndexClassView(ListView): #class based item views
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'data_item'

# this view is for details.html for displaying the details about a requested item
"""def detail(request, item_id):  #function based view
    item=Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request,'food/detail.html',context)"""
class FoodDetails(DetailView): #class based view
    model = Item
    template_name = 'food/detail.html'

# this views is used fpr forms.py where users can update data from the site

"""def create_item(request): #function based view
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form})"""

class CreateItem(CreateView):   #class based view for creating item
    model = Item
    fields = ['item_name','item_desc','item_price','item_img']
    template_name = 'food/item-form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)
    
# views for updating data from site
def update(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.hrml', {'form':form, 'item':item})

# views for deleting item from site

def delete(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/item-delete.html', {'item':item})