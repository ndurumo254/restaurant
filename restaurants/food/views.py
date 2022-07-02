from pickle import NONE
from django.shortcuts import redirect, render
from.models import Item
from.forms import Itemdetail

# Create your views here.
def index(request):
    item=Item.objects.all()
    context={
        "item":item
    }
    return render(request,"food/index.html",context)

def detail(request,id):
    item=Item.objects.get(id=id)
    return render(request, "food/details.html",{'item':item})


def create_item(request):
    form=Itemdetail(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")

    return render (request, "food/item-add.html", {'form':form})
