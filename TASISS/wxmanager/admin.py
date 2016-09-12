from django.contrib import admin
from django import forms
import django.core.exceptions as djexception
from .models import Ob_opening, Register
# Register your models here.


class RegisterInlineForm(forms.ModelForm):
    def clean_ob_opening(self):
        ob_opening = self.cleaned_data['ob_opening']
        if ob_opening.register_set.exclude(pk=self.instance.pk).count() == ob_opening.max_num:
            raise djexception.ValidationError('Reaching maximum resevation.')
        return ob_opening


class RegisterInline(admin.TabularInline):
    model = Register
    extra = 0
    form = RegisterInlineForm


class Ob_openingAdmin(admin.ModelAdmin):
    list_display = ('name', 'starttime', 'endtime')
    list_filter = ['starttime']
    inlines = [RegisterInline]

admin.site.register(Ob_opening, Ob_openingAdmin)
