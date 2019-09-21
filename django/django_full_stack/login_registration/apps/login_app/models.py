from __future__ import unicode_literals
from django.contrib.auth.models import UserManager
from django.db import models
import re
import bcrypt

class user1Manager(models.Manager):
    def registration_validation(self, postData):
        errors = {}
        print('---------------------------')
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['emailerr1'] = ("Invalid email address!")
        # registering_user = postData['email']
        check_user_list = user1.objects.values_list('email', flat=True)
        if postData['email'] in check_user_list:
            errors['email_in_use'] = "Email is already registered."
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
        print('---------------------------')
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['lemail']):
            errors['emailerr1'] = ("Invalid email address!")
        if len(postData['lemail']) < 1:
            errors['emailerr2'] = "Email field is required."
        if len(postData['lpassword']) < 8:
            errors['lpassword'] = "Password field must contain at least 8 characters."
        user = user1.objects.get(email=postData['lemail'])
        if not user:
            errors['emailerr1'] = "Invalid email."
        else:
            if bcrypt.checkpw(postData['lpassword'].encode(), user.password.encode()):
                print("password match")
            else:
                errors['passwords'] = "Username and Password does not match."
        return errors

class user1(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.CharField(max_length=155)
    password = models.CharField(max_length=255)
    objects = user1Manager()