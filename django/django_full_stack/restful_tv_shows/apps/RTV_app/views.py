from django.shortcuts import render, redirect, HttpResponse
from .models import Show

def index(request):
    return redirect('/shows')

def AllShows(request):
    if request.method == "GET":
        showdata = Show.objects.all()
        context = {
            "all_shows": showdata,
        }
        return render(request, 'RTV_app/AllShows.html', context)
    if request.method == "POST":
        return redirect(f"/shows")

def AddNewShow(request):
    if request.method == "GET":
        return render(request, 'RTV_app/AddNewShow.html')
    if request.method == "POST":
        Show.objects.create(title=request.POST['Title'], network=request.POST['Network'], date=request.POST['ReleaseDate'], desc=request.POST['Description'])
        return redirect(f"/shows")

def EditShow2(request, edit_show):
    if request.method == "GET":
        context = {
            "show": Show.objects.get(id=edit_show)
        }
        return render(request, 'RTV_app/EditShow2.html', context)
    if request.method == "POST":
        editshow = Show.objects.get(id=edit_show)
        editshow.title=request.POST['Title']
        editshow.save()
        editshow.network=request.POST['Network']
        editshow.save()
        editshow.date=request.POST['ReleaseDate']
        editshow.save()
        editshow.desc=request.POST['Description']
        editshow.save()
        return redirect(f'/shows/{edit_show}')

def TVShow2(request, id):
    if request.method == "GET":
        context = {
            "described_show": Show.objects.get(id=id)
        }
        return render(request, 'RTV_app/TVShow2.html', context)

def Destroy(request, id):
    if request.method == "GET":
        destroydata = Show.objects.get(id=id)
        context = {
            "destroy": destroydata.delete()
        }
        return redirect('/shows')