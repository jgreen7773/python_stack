from django.shortcuts import render, redirect, HttpResponse
from .models import message, comment, user1, user1Manager
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib import messages
import bcrypt

def home(request):
    return redirect('/login')

def login(request):
    return render(request, 'wall_app/login.html')

def signup(request):
    return render(request, 'wall_app/signup.html')

def processregistration(request):
    errors = user1.objects.registration_validation(request.POST)
    if len(errors) > 0:
        for errors, value in errors.items():
            messages.error(request, value, extratags='registration_failed')
        return redirect('/')
    pw = request.POST['password']
    pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
    print(pw_hash)
    user = user1.objects.create(alias=request.POST['alias'], first_name=request.POST['f_name'], last_name=request.POST['l_name'], email=request.POST['email'], password=pw_hash)
    return redirect('/')

def processlogin(request):
    errors = user1.objects.login_validation(request.POST)
    if len(errors) > 0:
        for errors, value in errors.items():
            messages.error(request, value, extratags='login_failed')
        return redirect('/')
    user = user1.objects.filter(email=request.POST['lemail'])
    logged_user = user[0]
    if bcrypt.checkpw(request.POST['lpassword'].encode(), user[0].password.encode()):
        request.session['lemail'] = logged_user.id
        return redirect('/wall')
    return redirect('/')

def wall(request):
    if request.method == "GET":
        context = {
            #"a_messages": user1.posted_message,
            #"message_poster": message.message_poster,
            #"a_comments": user1.posted_comment,
            #"comment_poster": comment.comment_poster,
            "current_user": user1.objects.get(id=request.session['lemail']),
            "Messages":message.objects.all(),
            "Comments":comment.objects.all(),
        }
        print(context)
        request.session['post_message'] = []
        return render(request, 'wall_app/wall.html', context)
    if request.method == "POST":
        user = user1.objects.filter(email=request.session['lemail'])
        if user != request.session.get('lemail'):
            redirect('/')
        if 'message' not in request.POST:
            HttpResponse('Message not submitted')
        if 'message' in request.POST:
            newly_created_message = message.objects.create(message_poster=user1.objects.get(id=request.session['lemail']), message=request.POST['message'])
            request.session['post_message'].insert(0, newly_created_message)
            # if 'message' == message.objects.filter(message_poster=request.session.get['lemail']):
        if 'comment' not in request.POST:
            HttpResponse('Comment not submitted')
        if 'comment' in request.POST:
            comment.objects.create(comment_poster=user1.objects.get(id=request.session['lemail']), comment=request.POST['comment'])
            message_to_connect_comments_to = message.objects.get(id=)  message_commented_on=message_commented_on.message
        return redirect('/wall')

def delete(request):
    return redirect('/wall')

def logout(request):
    request.session.flush()
    try:
        del request.session['lemail']
    except KeyError:
        pass
    return redirect('/')
