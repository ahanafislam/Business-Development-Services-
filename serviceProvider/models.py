from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Provider_submit(models.Model):
    accept = models.BooleanField(default=False)
    reject = models.BooleanField(default=False)
    feedback = models.TextField(blank=True,null=True)
    submit_date = models.DateTimeField(default=datetime.now,blank= True)
    document = models.FileField(blank=True,null=True)
    feedbackFor = models.ForeignKey(User,on_delete=models.CASCADE)
