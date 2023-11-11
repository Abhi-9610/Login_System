from django.core.mail import send_mail
from django.conf import Settings, settings

from .models import CustomUser

from .views import *
from django.urls import reverse
def send_verification_email(user):
    
    

    subject = "Welcome to Our Site, " + user.first_name
    message = f"Hello {user.first_name},\n\nThank you for registering on our website. We are excited to have you as part of our community.\n\nBest regards,\nThe LoginSystem Team "
    
    from_email = settings.EMAIL_HOST_USER 
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)
