from __future__ import unicode_literals
from django.db import models
import datetime
import time

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        print('-------------------')
        if len(postData['Title']) < 2:
            errors['title'] = "Title should be atleast two characters."
        
        if len(postData['Network']) < 3:
            errors['Network'] = "Network should be atleast three characters."
        
        if len(postData['Description']) < 10:
            errors['description1'] = "Description should be atleast ten characters."
        
        # entered_date = datetime.datetime.strptime(postData['ReleaseDate'], "%Y-%a-%d").date()
        # today_date = datetime.date.today()
        
        # if entered_date > today_date:
        #     errors['releaseDate'] = "Date must be in the past."
        
        if len(postData['Description']) < 10 and len(postData['Description']) > 0:
            errors['description2'] = "Description should be atleast ten characters."
        
        return errors

class Show(models.Model):
    title = models.CharField(max_length=55)
    network = models.CharField(max_length=33)
    date = models.CharField(max_length=33)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    def __repr__(self):
        return f"Network: {self.title} {self.date}"
