from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=55)
    network = models.CharField(max_length=33)
    date = models.CharField(max_length=33)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"Network: {self.title} {self.date}"
