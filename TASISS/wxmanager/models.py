from django.db import models

# Create your models here.
class Ob_opening(models.Model):
    name = models.CharField(max_length=160)
    max_num = models.IntegerField(default=100)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()

class Register(models.Model):
    ob_opening = models.ForeignKey(Ob_opening, on_delete=models.CASCADE)
    openid = models.CharField(max_length=100)
    signed = models.IntegerField(default=0)
