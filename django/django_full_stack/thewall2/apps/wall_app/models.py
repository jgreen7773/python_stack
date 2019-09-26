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
            errors['correct_email_format_registration'] = ("Invalid email address!")
        check_user_list = user1.objects.values_list('email', flat=True)
        if postData['email'] in check_user_list:
            errors['email_in_use_check_registration'] = "Please choose another email."
        if len(postData['f_name']) < 2:
            errors['insufficient_length_firstname'] = "First name should contain at least 2 characters."
        elif len(postData['f_name']) < 1:
            errors['empty_field_firstname'] = "First Name field is required."
        if len(postData['l_name']) < 2:
            errors['insufficient_length_lastname'] = "Last name should contain at least 2 characters."
        elif len(postData['l_name']) < 1:
            errors['empty_field_lastname'] = "Last Name field is required."
        if len(postData['email']) < 1:
            errors['empty_field_email_registration'] = "Email field is required."
        if len(postData['password']) < 8:
            errors['insufficient_length_password_registration'] = "Password field must contain at least 8 characters."
        if postData['password'] != postData['cpassword']:
            errors['matching_password_registration_check'] = "Passwords must match!"
        return errors
    def login_validation(self, postData):
        errors = {}
        print('---------------------------')
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['lemail']):
            errors['correct_email_format_login'] = ("Invalid email address!")
        if len(postData['lemail']) < 1:
            errors['empty_field_email_login'] = "Email field is required."
        if len(postData['lpassword']) < 8:
            errors['insufficient_length_password_login'] = "Password field must contain at least 8 characters."
        user = user1.objects.filter(email=postData['lemail'])
        if not user:
            errors['email_is_registered_login_check'] = "Invalid email."
        else:
            if bcrypt.checkpw(postData['lpassword'].encode(), user[0].password.encode()):
                print("password match")
            else:
                errors['Invalid_email_password_combination'] = "Username and Password does not match."
        return errors

# class messageManager(models.Manager):
#     def add_message_validator(self, postData):
#         errors = {}
#         print('-------------------')
#         if len(postData['']) == 0:
#             errors[''] = " must be provided."
#         if len(postData['']) < 3:
#             errors[''] = " should be atleast three characters."
#         if len(postData['']) == 0:
#             errors[''] = " must be provided."
#         if len(postData['']) < 3:
#             errors[''] = " should be atleast three characters."
#         if len(postData['']) == 0:
#             errors[''] = " must be provided."
#         if len(postData['']) < 3:
#             errors[''] = " should be atleast three characters."
#         return errors
#     def add_comment_validator(self, postData):
#         errors = {}
#         print('-------------------')
#         if len(postData['']) == 0:
#             errors[''] = " must be provided."
#         if len(postData['']) < 3:
#             errors[''] = " should be atleast three characters."
#         if len(postData['']) == 0:
#             errors[''] = " must be provided."
#         if len(postData['']) < 3:
#             errors[''] = " should be atleast three characters."
#         if len(postData['']) == 0:
#             errors[''] = " must be provided."
#         if len(postData['']) < 3:
#             errors[''] = " should be atleast three characters."
#         return errors

class user1(models.Model):
    alias = models.CharField(max_length=44)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.CharField(max_length=155)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = user1Manager()

class message(models.Model):
    message_poster = models.ForeignKey(user1, related_name="posted_message")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = messageManager()

class comment(models.Model):
    message_commented_on = models.ForeignKey(message, related_name="reply")
    comment_poster = models.ForeignKey(user1, related_name="posted_comment")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = commentManager()