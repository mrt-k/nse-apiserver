from django.contrib import admin
from api.models import NseArgv, Nse

class NseArgvAdmin(admin.ModelAdmin):
    pass


class NseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

admin.site.register(NseArgv, NseArgvAdmin)
admin.site.register(Nse, NseAdmin)
