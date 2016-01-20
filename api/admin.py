from django.contrib import admin
from api.models import NseArgv, Nse
from django import forms

class NseArgvAdmin(admin.ModelAdmin):
    pass


class NseAdmin(admin.ModelAdmin):

    class Meta:
        ordering = ['argvs']

    list_display = ('name', 'category')

admin.site.register(NseArgv, NseArgvAdmin)
admin.site.register(Nse, NseAdmin)
