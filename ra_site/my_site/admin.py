from django.contrib import admin

# Register your models here.

from .models import AcidInfo, RecksonInfo, Gameprogress

admin.site.register(AcidInfo)
admin.site.register(RecksonInfo)
admin.site.register(Gameprogress)

