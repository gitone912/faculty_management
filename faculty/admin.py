from django.contrib import admin
from .models import Subject, Course, TeachingRecord, UserProfile

# Change the admin site header to "ICFAI Administrator"
admin.site.site_header = "ICFAI Administrator"
admin.site.index_title = "ICFAI Administration"

# Create a custom admin class for each model to display full details in the admin interface

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Display these fields in the list view
    search_fields = ('name',)  # Allow searching by name
    list_filter = ('name',)  # Allow filtering by name

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Display these fields in the list view
    search_fields = ('name',)  # Allow searching by name
    list_filter = ('name',)  # Allow filtering by name

class TeachingRecordAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'subject', 'course', 'topic_taught', 'salary', 'start_time', 'end_time')  # Display these fields in the list view
    search_fields = ('faculty__username', 'subject__name', 'course__name', 'topic_taught')  # Allow searching by faculty, subject, course, or topic
    list_filter = ('faculty', 'subject', 'course', 'start_time', 'end_time')  # Allow filtering by these fields

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'experience')  # Display these fields in the list view
    search_fields = ('user__username',)  # Allow searching by username
    list_filter = ('experience',)  # Allow filtering by experience

# Register each model with its custom admin class
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(TeachingRecord, TeachingRecordAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
