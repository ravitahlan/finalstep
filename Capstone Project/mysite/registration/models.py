from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserModel(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,
        primary_key=True)

    #extra added field
    accountType = models.CharField(max_length = 30)

    def getAccountType(self):
        return self.accountType

    def __str__(self):
        return self.accountType+" : "+ self.user.username
