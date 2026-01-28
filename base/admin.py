from django.contrib import admin
from base.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','subject']
admin.site.register(Student,StudentAdmin)
