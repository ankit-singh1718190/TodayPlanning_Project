from django.contrib import admin
from .models import devPlanning
# Register your models here.
@admin.register(devPlanning)
class devmodeladmin(admin.ModelAdmin):
    list_display=['id','item']