from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import UserManager
import re
import bcrypt

class UserManager(models.Manager):
    def registration_validation(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['correct_email_format'] = ("Invalid email address!")
        check_user_list = User.objects.values_list('email', flat=True)
        if postData['email'] in check_user_list:
            errors['email_in_use'] = "Please choose another email."
        if len(postData['f_name']) < 2:
            errors['first'] = "First name should contain at least 2 characters."
        elif len(postData['f_name']) < 1:
            errors['field_first'] = "First Name field is required."
        if len(postData['l_name']) < 2:
            errors['last'] = "Last name should contain at least 2 characters."
        elif len(postData['l_name']) < 1:
            errors['field_last'] = "Last Name field is required."
        if len(postData['email']) < 1:
            errors['emailerr2'] = "Email field is required."
        if len(postData['password']) < 8:
            errors['password'] = "Password field must contain at least 8 characters."
        if postData['password'] != postData['cpassword']:
            errors['passwords'] = "Passwords must match!"
        return errors
    def login_validation(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['lemail']):
            errors['not_registered'] = ("Invalid email address!")
        if len(postData['lemail']) < 1:
            errors['blank_field'] = "Email field is required."
        if len(postData['lpassword']) < 8:
            errors['password_strength_security'] = "Password field must contain at least eight characters."
        user = User.objects.filter(email=postData['lemail'])
        if not user:
            errors['not_registered'] = "Invalid email address entered, or the id is not registered."
        else:
            if bcrypt.checkpw(postData['lpassword'].encode(), user[0].password.encode()):
                print("----------------")
                print("Passwords match!")
                print("----------------")
            else:
                errors['invalid_password_email_match'] = "Invalid Username or Password."
        return errors

class MessageManager(models.Manager):
    def post_message_validation(self, postData):
        errors = {}
        if len(postData['typemessage']) < 2:
            errors['spam_guard_post_length'] = "Please enter at least two characters...."
        return errors

class CommentManager(models.Manager):
    def comment_message_validation(self, postData):
        errors = {}
        if len(postData['typecomment']) < 2:
            errors['meaningful_response'] = "Please post more than two characters, encouraging more meaningful responses."
        return errors
    def reply_message_validation(self, postData):
        errors = {}
        if len(postData['typereply']) < 2:
            errors['meaningful_response'] = "Please post more than two characters, encouraging more meaningful responses."
        return errors

class User(models.Model):
    alias = models.CharField(max_length=44)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.CharField(max_length=155)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    posted_by = models.ForeignKey(User, related_name="poster", default=None)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class Comment(models.Model):
    replied_by = models.ForeignKey(Message, related_name="message_replied_on", default=None)
    commenter = models.ForeignKey(User, related_name="user_commented_to", default=None)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()