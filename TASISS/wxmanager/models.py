from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Ob_opening(models.Model):
    name = models.CharField(max_length=160, blank=False)
    max_num = models.PositiveIntegerField(default=100, blank=False)
    starttime = models.DateTimeField(blank=False)
    endtime = models.DateTimeField(blank=False)

    # Validation
    def clean(self):
        super(Ob_opening, self).clean()
        if self.starttime > self.endtime:
            raise ValidationError('Start time must be latter than end time')
        

class Register(models.Model):
    ob_opening = models.ForeignKey(Ob_opening, on_delete=models.CASCADE)
    openid = models.CharField(max_length=100, blank=False)
    signed = models.IntegerField(default=0, blank=False)
