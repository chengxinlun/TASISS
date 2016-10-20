from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Ob_opening(models.Model):
    name = models.CharField(max_length=160, blank=False)
    max_num = models.PositiveIntegerField(default=100, blank=False)
    # Reservation
    starttime = models.DateTimeField(blank=False)
    endtime = models.DateTimeField(blank=False)
    # Checkin
    startcheckin = models.DateTimeField(blank=False)
    endcheckin = models.DateTimeField(blank=False)

    # Validation
    def clean(self):
        super(Ob_opening, self).clean()
        if self.starttime > self.endtime:
            raise ValidationError('Reservation start time must be earlier than end time')
        if self.endtime > self.startcheckin:
            raise ValidationError('Reservation end time must be earlier than checkin start time')
        if self.startcheckin > self.endcheckin:
            raise ValidationError('Checkin start time must be earlier than end time')


class Register(models.Model):
    ob_opening = models.ForeignKey(Ob_opening, on_delete=models.CASCADE)
    openid = models.CharField(max_length=100, blank=False)
    signed = models.IntegerField(default=0, blank=False)
