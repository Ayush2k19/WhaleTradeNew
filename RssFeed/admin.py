from django.contrib import admin
from .models import *


#class PostAdmin(admin.ModelAdmin):
   # list_display = ('title', 'body',)
    #list_editable = ('title' , 'body' ,)
MyModels =[ Post, Telegram , Twitter , Youtube , Discord]    


admin.site.register( MyModels)
