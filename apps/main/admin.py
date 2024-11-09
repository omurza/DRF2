from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(NewsKg)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields=['id','desctiption']
    list_filter=['id','title']
      