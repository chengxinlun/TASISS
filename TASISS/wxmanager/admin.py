from django.contrib import admin
from .models import Ob_opening, Register
# Register your models here.

class RegisterInline(admin.TabularInline):
    model = Register
    extra = 0


class Ob_openingAdmin(admin.ModelAdmin):
    list_display = ('name', 'starttime', 'endtime')
    list_filter = ['starttime']
    inlines = [RegisterInline]

admin.site.register(Ob_opening, Ob_openingAdmin)
