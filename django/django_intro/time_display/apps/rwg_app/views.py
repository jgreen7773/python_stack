from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    if request.method == "GET":
        return render(request, "rwg_app/rwg.html")
    if request.method == "POST":
        string = get_random_string(length=14)
        request.session['string'] = string
        request.session['counter'] += 1
        return redirect("/rwg/")

def reset(request):
    request.session.clear()
    return redirect('/rwg/reset')