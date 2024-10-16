from django.contrib import admin
from .models import *

# Register your models here.




@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'user__email', 'matric_no']
    list_display = ['user', 'matric_no']
    actions = ['mark_as_verified']

    def mark_as_verified(self, request, queryset):
        queryset.update(is_verified=True)
    mark_as_verified.short_description = "Mark selected profiles as verified"


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']


@admin.register(CourseScores)
class CourseScoresAdmin(admin.ModelAdmin):
    search_fields = ['student']
    list_display = ['student']


# Customize the admin site
admin.site.site_header = "PTI Student Records Management System"
admin.site.site_title = "PTI Student Records Management System"
admin.site.index_title = "Welcome to PTI Student Records Management System"
admin.site.app_label = "Student Records Management System"
admin.site._registry[Faculty].verbose_name = "Faculty"
admin.site._registry[Faculty].verbose_name_plural = "Faculties"
