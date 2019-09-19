from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Show, ShowManager

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
    else:
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for errors, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        else:
            Show.objects.create(title=request.POST['Title'], network=request.POST['Network'], date=request.POST['ReleaseDate'], desc=request.POST['Description'])
            return redirect(f"/shows")

def EditShow2(request, edit_show):
    if request.method == "GET":
        context = {
            "show": Show.objects.get(id=edit_show)
        }
        return render(request, 'RTV_app/EditShow2.html', context)
    else:
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for errors, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{edit_show}/edit')
        editshow = Show.objects.get(id=edit_show)
        editshow.title = request.POST['Title']
        editshow.network = request.POST['Network']
        editshow.date = request.POST['ReleaseDate']
        editshow.desc = request.POST['Description']
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

# def update(request, id):
#     errors = Show.objects.basic_validation(request.POST)
#     if len(errors) > 0:
#         for , value in errors.items():
#             messages.error(request, value)
#         return redirect('/shows/new')
#     else:
#         show = Show.objects.get(id=id)
#         show.title = request.POST['Title']
#         show.network = request.POST['Network']
#         show.date = request.POST['ReleaseDate']
#         show.desc = request.POST['Description']
#         show.save()
#         messages.success(request, "Show has been added!")
#         return redirect('/shows')
