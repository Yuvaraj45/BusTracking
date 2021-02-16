from django.contrib import admin
from .models import bus,track,user_profile
# Register your models here.
class busmodel(admin.ModelAdmin):
	list_display = ['title']

class profilemodel(admin.ModelAdmin):
	list_display = ['user','dob']

admin.site.register(track)
admin.site.register(bus,busmodel)
admin.site.register(user_profile,profilemodel)

