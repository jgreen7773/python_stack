from django.shortcuts import render, redirect, HttpResponse
from .models import user1, user1Manager
from django.contrib import messages
import bcrypt

def index(request):
    if request.method == "GET":
        return render(request, 'login_app/login_registration.html')

def processreg(request):
    errors = user1.objects.registration_validation(request.POST)
    if len(errors) > 0:
        for errors, value in errors.items():
            messages.error(request, value, extra_tags='registration_fail')
        return redirect('/')
    pw = request.POST['password']
    pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
    print(pw_hash)
    user = user1.objects.create(first_name=request.POST['f_name'], last_name=request.POST['l_name'], email=request.POST['email'], password=pw_hash)
    return redirect('/')

def processlog(request):
    errors = user1.objects.login_validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='login_fail')
        return redirect('/')
    user = user1.objects.filter(email=request.POST['lemail'])
    logged_user = user[0]
    if bcrypt.checkpw(request.POST['lpassword'].encode(), logged_user.password.encode()):
        request.session['lemail'] = logged_user.id
        return redirect('/success')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def success(request):
    context = {
        "logged_user": user1.objects.get(id=request.session['lemail'])
    }
    return render(request, 'login_app/success.html', context)