from django.shortcuts import render, redirect, HttpResponse
from .models import User, UserManager
from django.contrib import messages
import bcrypt

def index(request):
    if request.method == "GET":
        return render(request, 'login_app/login.html')
        pw = request.POST['password']
        pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        print(pw_hash)
        user = User.objects.create(first_name=request.POST['f_name'], last_name=request.POST['l_name'], email=request.POST['email'], password=request.POST['password'])
        request.session['email'] = user.email
        HttpResponse("Successfully registered!")
        return redirect('/')

def success(request):
    errors = User.objects.login_validation(request.POST)
    if len(errors) > 0:
        for errors, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        return render(request, 'login_app/success.html')
