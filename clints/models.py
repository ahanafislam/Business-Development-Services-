from django.db import models
from django.contrib.auth.models import User
from account.models import CompanyDetails
from datetime import datetime

class Submit_document(models.Model):
    title = models.CharField(max_length=255)
    submit_date = models.DateTimeField(default=datetime.now,blank= True)
    description = models.TextField()
    rajuk = models.FileField(blank=True,null=True,upload_to='submited/files/')
    rajukChk = models.BooleanField(default=False)
    wasa = models.FileField(blank=True,null=True,upload_to='submited/files/')
    bangladeshBank = models.FileField(blank=True,null=True,upload_to='submited/files/')
    titas = models.FileField(blank=True,null=True,upload_to='submited/files/')
    pdb = models.FileField(blank=True,null=True,upload_to='submited/files/')
    comments = models.TextField(blank=True,null=True)
    accept = models.BooleanField(default=False)
    submitor = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:100]

    def submit_date_pretty(self):
        return self.submit_date.strftime('%d.%m.%y')
