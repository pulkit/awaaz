from django.contrib import admin
from videos.models import *

class VideoAdmin(admin.ModelAdmin):
    pass

admin.site.register(video,VideoAdmin)
admin.site.register(Category)
