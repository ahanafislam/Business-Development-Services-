from django.db import models
from django.contrib.auth.models import User

class ServiceProviderList(models.Model):
    title = models.CharField(default='',max_length=255)
    description = models.TextField()
    url = models.TextField(blank=True)
    icon = models.ImageField(upload_to='images/')
    provider = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class CompanyDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='companyDetails')
    company_name = models.CharField(default='',max_length=255)
    website = models.TextField(default='',max_length=255)
    street_address = models.CharField(default='',max_length=255)
    city = models.CharField(default='',max_length=255)
    state = models.CharField(default='',max_length=255)
    zip_code = models.CharField(default='',max_length=255)
    country = models.CharField(default='',max_length=255)
    logo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.company_name
