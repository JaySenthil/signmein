from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    #pass
    # add additional fields in here
    orgName = models.TextField(unique = True)
    orgNameUrl = models.TextField(unique = True)
    def __str__(self):
        return self.username

class Meetings(models.Model):
    organization = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.organization.orgName

class Members(models.Model):
    name = models.CharField(max_length=128)
    orgRef = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    meetRef = models.ForeignKey(Meetings, on_delete=models.CASCADE)
    def __str__(self):
        return self.orgRef.orgName
