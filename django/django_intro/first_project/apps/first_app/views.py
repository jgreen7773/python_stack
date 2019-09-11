from django.shortcuts import render, HttpResponse, redirect
# def old_index(request):
#     return HttpResponse("this is the equivalent of @app.route('/')!")
# Create your views here.
def index(request, id):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("blah blah blah")

def show(request, id):
    return HttpResponse("The number you entered is:" + str(id))

def edit(request, id):
    return HttpResponse("The number you entered is:" + str(id))

def destroy(request, id):
    return redirect("Hey again this is the destroy method.")