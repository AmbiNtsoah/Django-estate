from django.shortcuts import render, redirect
from .models import Details
from .form import HotelForm

# Create your views here.
def details(request):
    """ ORM django pour recupérer TOUS les donnée de notre class Details """
    appart_details = Details.objects.all()
    context = {
        "appart_details": appart_details
    }
    return render (request, "index.html", context)

def read_details(request, pk):
    """ ORM de Django pour Lire (READ) des donnée de notre class Details """
    read = Details.objects.get(id=pk)
    context = {
        "read": read
    }
    return render(request, "moreInfo.html", context)

def create_hotels(request):
    new = HotelForm()
    if request.method == "POST":
        new = HotelForm(request.POST, request.FILES)
        if new.is_valid():
            new.save()
            return redirect("/")
    context = {
        "new": new
    }
    return render(request, "create.html", context)

def update_details(request, pk):
    update = Details.objects.get(id=pk)
    new = HotelForm(instance=update)
    if request.method == "POST":
        new = HotelForm(request.POST, instance=update, files=request.FILES)
        if new.is_valid():
            new.save()
            return redirect("/")
    context = {
        "new": new
    }
    return render(request, "update.html", context)

def delete_estate(request, pk):
    estate = Details.objects.get(id=pk)
    estate.delete()
    return redirect ("/")