from django.apps import AppConfig


class FacultyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "faculty"
    
    def ready(self):
        from faculty import signals  # Import the signals module to register the signal handler
