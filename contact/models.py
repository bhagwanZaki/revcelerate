# contacts/models.py

from django.db import models
from django.core.validators import RegexValidator


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    # optional fields
    mobile_num_regex  = RegexValidator(regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!")
    mobile_number  = models.CharField(validators=[mobile_num_regex], max_length=13,unique=True,blank=True)
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    instagram_handle = models.CharField(max_length=255, blank=True)
    companies = models.ManyToManyField(Company, related_name='contacts')

    def __str__(self):
        return self.name
