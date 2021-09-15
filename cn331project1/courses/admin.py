from django.contrib import admin

# Register your models here.

from .models import CourseModel
class CourseModelAdmin(admin.ModelAdmin):
    filter_horizontal = ("student",)

admin.site.register(CourseModel, CourseModelAdmin)