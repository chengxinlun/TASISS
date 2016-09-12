from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
class Member(models.Model):
    openid = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=30)
    # Gender
    gender_choice = (
        ('f', _('genderFemale')),
        ('m', _('genderMale')),
        )
    gender = models.CharField(max_length=1, choices=gender_choice, default='f')
    # Working department in society
    wd_choice = (
        ('co', _('departmentCouncil')),
        ('ma', _('departmentManagement')),
        ('fa', _('departmentForeignaffair')),
        ('ia', _('departmentInternalaffair')),
        ('pr', _('departmentPropogenda')),
        ('ac', _('departmentAcademic')),
        )
    wd = models.CharField(max_length=2, choices=wd_choice, default='ac')
    # Working position in society
    wp_choice = (
        ('mc', _('positionMemberofcouncil')),
        ('le', _('positionLeader')),
        ('vl', _('positionViceleader')),
        ('hd', _('positionHeadofdepartment')),
        ('vh', _('positionVicehead')),
        ('md', _('positionMemberofdepartment')),
        )
    wp = models.CharField(max_length=2, choices=wp_choice, default='md')

    def __str__(self):
        return self.name
