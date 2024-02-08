from django.db import models
from accounts import models as account_model
# Create your models here.
class sport(models.Model):
    name=models.CharField(max_length=20,default="")
    ava=models.IntegerField(default=0)
class issued(models.Model):
    user=models.ForeignKey(account_model.CustomUser, on_delete=models.CASCADE)
    sporting=models.ForeignKey(sport,on_delete=models.SET_NULL,null=True,blank=True)
    accept=models.BooleanField(default=False)
    cancel=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)
    issued_number=models.IntegerField(default=0)