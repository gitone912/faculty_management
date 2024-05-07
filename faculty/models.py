# In faculty_management/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db.models import Sum
# import User
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # Link this profile to the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # Add the experience field (years of experience)
    experience = models.PositiveIntegerField(default=0, help_text='Years of experience')
    
    def __str__(self) -> str:
        return self.user.username

class Subject(models.Model):
    name = models.CharField(max_length=100)  # Name of the subject
    description = models.TextField(blank=True, null=True)  # Description of the subject

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)  # Name of the course
    description = models.TextField(blank=True, null=True)  # Description of the course

    def __str__(self):
        return self.name

class TeachingRecord(models.Model):
    """
    TeachingRecord model to record teaching activities by faculty.
    """
    faculty = models.ForeignKey(User, on_delete=models.CASCADE,)  # Link to faculty user
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)  # Link to subject
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Link to course
    topic_taught = models.CharField(max_length=255)  # Topic taught by faculty
    salary = models.DecimalField(max_digits=6, decimal_places=2, default=300.00)  # Salary per class taught
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)  # Add the description field

    @property
    def salary(self):
        # Access the faculty's profile to retrieve their experience
        experience = self.faculty.profile.experience if self.faculty.profile else 0
        # Determine salary based on experience
        if experience >= 5:
            return 500.00  # Salary if experience is 5 years or more
        else:
            return 350.00  # Salary if experience is less than 5 years
        
    def __str__(self):
        return f"{self.faculty.username} - {self.subject.name} - {self.course.name} - {self.topic_taught} on {self.start_time}"

