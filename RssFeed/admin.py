from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    #list_editable = ('title' , 'body' ,)
    


admin.site.register( Post , PostAdmin)
