from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    if request.method == "GET":
        return render(request, 'login_app/login_registration.html')
    else:
        return redirect('/')

def processreg(request):
    errors = User.objects.login_validation(request.POST)
    if len(errors) > 0:
        for errors, value in errors.items():
            messages.error(request, value, extra_tags='registration_fail')
        return redirect('/')
    else:
        pw = request.POST['password']
        pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        print(pw_hash)
        user = User.objects.create(first_name=request.POST['f_name'], last_name=request.POST['l_name'], email=request.POST['email'], password=pw_hash)
        return redirect('/')

def processlog(request):
    errors = User.objects.login_validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='login_fail')
        return redirect('/')
    else:
        user = User.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['email'] = logged_user.id
                return redirect('/success')
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def success(request):
    return render(request, 'login_app/success.html')