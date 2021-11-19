from django.db import models
from django.urls import reverse
# Create your models here.
class company(models.Model):
    company_name=models.CharField(max_length=30)
    company_logo=models.FileField(null='true',blank='true')
    company_city=models.CharField(max_length=30,)

    def __str__(self):
        return self.company_name
    def get_absolute_url(self):
        return reverse('retrive',kwargs={'id':self.id})