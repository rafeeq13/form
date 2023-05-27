from django.contrib import admin
from .models import Apply,AddJob,Info
# Register your models here.
@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    list_display=['name','email','contact','address','education','obtained_marks','total_marks','apply','resume']


@admin.register(AddJob)
class AddJobAdmin(admin.ModelAdmin):
    list_display=['jobtitle','job_description','requirements','add','deadline']



@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display=['name','size','location']