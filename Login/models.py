from django.db import models

class CustomUser(models.Model):
    # Other fields (e.g., username, email, etc.)

    verification_token = models.CharField(max_length=100, blank=True, null=True)
