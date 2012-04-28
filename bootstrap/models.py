from django.db import models
from django.contrib.auth.models import User

class ObieConnectProfile(models.Model):
    user = models.OneToOneField(User, related_name='obieconnectprofile')
    bio = models.TextField(max_length=500)
    activation_key = models.CharField(max_length=40)
    key_expires = models.DateTimeField()
    def __unicode__(self):
        return self.username

class ExampleFields(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    password_confirm = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name
        
class Course(models.Model):
    crn = models.IntegerField(max_length=5, blank=False)
    level = models.IntegerField(max_length=3, blank=False)
    name = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=500)
    def __unicode__(self):
        return self.name
    
class Professor(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    office = models.CharField(max_length=100)
    def __unicode__(self):
	return self.lastname
    
class Department(models.Model):
    fullname = models.CharField(max_length=30)
    shortname = models.CharField(max_length=4)
    def __unicode__(self):
	return self.shortname
