from __future__ import unicode_literals
from django.db import models
import re


class UserManager(models.Manager):
    def login_validation(self, request, postData):
        errors = {}
        print('---------------------------')
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(request.form['email']):
            errors['email'] = ("Invalid email address!")
        if len(postData['f_name']) < 2:
            errors['first'] = "First name should contain at least two characters."
        elif len(postData['f_name']) < 1:
            errors['field_first'] = "First Name field is required."
        if len(postData['l_name']) < 2:
            errors['last'] = "Last name should contain at least two characters."
        elif len(postData['l_name']) < 1:
            errors['field_last'] = "Last Name field is required."
        if len(postData['email']) < 1:
            errors['email'] = "Email field is required."
        if len(postData['password']) < 8:
            errors['password'] = "Password field must contain at least 8 characters."
        if postData['password'] != postData['cpassword']:
            errors['passwords'] = "Passwords must match!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.CharField(max_length=155)
    password = models.CharField(max_length=255)
    objects = UserManager()