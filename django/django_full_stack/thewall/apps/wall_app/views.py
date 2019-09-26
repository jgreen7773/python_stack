from django.shortcuts import render, redirect, HttpResponse
from .models import Message, Comment, User, MessageManager, CommentManager, UserManager
from django.contrib import messages
import bcrypt

def home(request):
    return redirect('/login')

def login(request):
    return render(request, 'wall_app/login.html')

def signup(request):
    return render(request, 'wall_app/signup.html')

def processregistration(request):
    errors = User.objects.registration_validation(request.POST)
    if len(errors) > 0:
        for errors, value in errors.items():
            messages.error(request, value, extra_tags='registration_failed')
        return redirect('/')
    pw = request.POST['password']
    pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
    print(pw_hash)
    user = User.objects.create(alias=request.POST['alias'], first_name=request.POST['f_name'], last_name=request.POST['l_name'], email=request.POST['email'], password=pw_hash)
    return redirect('/wall')

def processlogin(request):
    errors = User.objects.login_validation(request.POST)
    if len(errors) > 0:
        for errors, value in errors.items():
            messages.error(request, value, extra_tags="login_failed")
        return redirect('/')
    user = User.objects.filter(email=request.POST['lemail'])
    logged_user = user[0]
    if bcrypt.checkpw(request.POST['lpassword'].encode(), logged_user[0].password.encode()):
        request.session['lemail'] = logged_user.id
        return redirect('/wall')
    return redirect('/')

def processmessage(request):
    errors = Message.objects.post_message_validation(request.POST)
    if len(errors) > 0:
        for errors, value in errors.items():
            messages.error(request, value, extra_tags="post_message_requirements")
        return redirect('/')
    logged_user = User.objects.filter(email=request.session['lemail'])
    input_message = Message.objects.create(message=request.POST['typemessage'], posted_by=logged_user)
    request.session['post_message_list'].insert(0, input_message)
    # if 'typemessage' not in request.session:
    #     message = Message.objects.filter(message=request.POST['typemessage'])
    #     logged_message = message[0]
        # request.session['typemessage'] = logged_message.id
        # request.session['post_message_list'].insert(0, message)
    # stored_message = request.session.input_message
    # logged_user.poster.add(message=input_message)
    return redirect('/wall')

# logged_user.poster.message
# logged_user.commenter.comment
# logged_user.commenter.comment

def processcomment(request):
    errors = Comment.objects.comment_message_validation(request.POST)
    if len(errors) > 0:
        for errors, value in errors.items():
            messages.error(request, value, extra_tags="post_reply_requirements")
        return redirect('/')
    logged_user = User.objects.filter(id=request.session['lemail'])
    input_comment = Comment.objects.create(comment=request.POST['typecomment'], replied_by=Message.objects.get(posted_by=logged_user, commenter=logged_user))
    request.session['post_comment_list'].insert(0, input_comment)
    # if 'typecomment' not in request.session:
    #     comment = Comment.objects.filter(comment=request.POST['typecomment'])
    #     logged_comment = comment[0]
        # request.session['typecomment'] = logged_comment.id
        # request.session['post_comment_list'].insert(0, comment)
    # stored_comment = request.session.input_comment
    # logged_user.commenter.add(comment=input_comment)
    return redirect('/wall')

def processreply(request):
    errors = Comment.objects.reply_message_validation(request.POST)
    if len(errors) > 0:
        for errors, value in errors.items():
            messages.error(request, value, extra_tags="post_reply_requirements")
        return redirect('/')
    logged_user = User.objects.filter(id=request.session['lemail'])
    input_reply = Comment.objects.create(comment=request.POST['typereply'], replied_by=Message.objects.get(posted_by=logged_user), commenter=logged_user)
    request.session['post_reply_list'].insert(0, input_reply)
    # if 'typereply' not in request.session:
    #     reply = Comment.objects.filter(comment=request.POST['typereply'])
    #     logged_reply = reply[0]
        # request.session['typereply'] = logged_reply.id
        # request.session['post_reply_list'].insert(0, reply)
    # stored_reply = request.session.input_reply
    # logged_user.replier.add(comment=input_reply)
    return redirect('/wall')

def wall(request):
    if request.method == "POST":
        return redirect('/')
    if request.method == "GET":
        logged_user = User.objects.filter(id=request.session['lemail'])
        context = {
            "current_user": logged_user,
            "user_messages": Message.objects.all()
        }
        request.session['post_message_list'] = []
        request.session['post_comment_list'] = []
        request.session['post_reply_list'] = []
        return render(request, 'wall_app/wall.html', context)

def logout(request):
    request.session.flush()
    try:
        del request.session['lemail']
    except KeyError:
        pass
    return redirect('/')

def delete(request):
    # request.session.flush()
    return redirect('/wall')