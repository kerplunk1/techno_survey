from django.db import models

# Create your models here.

class Mails(models.Model):
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    login = models.CharField(max_length=25, unique=True)
    ya_app_pass = models.CharField(max_length=20)
    tmail_pass = models.CharField(max_length=20)
    sync = models.BooleanField(null=True)

    def __str__(self):
        return self.login

