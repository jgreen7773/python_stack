from django.shortcuts import render, redirect, HttpResponse
from .models import Show, Network

def AllShows(request):
    if request.method == "GET":
        showdata = Show.objects.all()
        networkdata = Network.objects.all()
        context = {
            "all_shows": showdata,
            "all_networks": networkdata,
        }
        return render(request, 'RTV_app/AllShows.html', context)
    if request.method == "POST":
        return redirect(f"/shows")

def AddNewShow(request):
    if request.method == "GET":
        return render(request, 'RTV_app/AddNewShow.html')
    if request.method == "POST":
        return redirect(f"/shows/{id}")

def EditShow2(request, id):
    if request.method == "GET":
        return render(request, 'RTV_app/EditShow2.html')
    if request.method == "POST":
        return redirect(f"/shows/{id}")

def TVShow2(request, id):
    if request.method == "GET":
        return render(request, 'RTV_app/TVShow2.html')

def Destroy(request, id):
    if request.method == "GET":
        destroydata = Show.objects.get(removed_id=id).remove(id)
        context = {
            "destroy": destroydata
        }
        return render(request, 'RTV_app/AllShows.html', context)
    if request.method == "POST":
        return redirect('/shows')