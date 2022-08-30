from django.contrib import admin
from .models import User, Video, WatchList, Comment, Topic

admin.site.register(User)
admin.site.register(WatchList)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Topic)
