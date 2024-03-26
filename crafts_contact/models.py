from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.core.validators import validate_email
from django.core.validators import MinLengthValidator


# Some help with choices field option was collected from https://stackoverflow.com/questions/18676156/how-to-properly-use-the-choices-field-option-in-django
class Contact(models.Model):
    class ContactChoices(models.TextChoices):
        REPORT = "1", "Business inquiries"
        BUSINESS = "2", "Report user"
        FEEDBACK = "3", "Feedback about website"
        OTHER = "4", "Other questions"
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(validators=[validate_email], blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(max_length=2200, null=False, blank=False, 
                               validators=[MinLengthValidator(5)])
    ContactChoices = models.CharField(
        max_length=1,
        choices=ContactChoices.choices,
        default=ContactChoices.OTHER,
        null=False
        )

    def __str__(self):
        return self.name + " - " + self.subject
    
    def send_confirmation_email(self):
        subject = "Thank you for your email"
        message = "Thank you for contacting us. We will get back to you as soon as possible."
        sender_email = self.email

        send_mail(
            subject=subject,
            message=message,
            from_email=sender_email,
            recipient_list=[settings.EMAIL_HOST_USER],
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.send_confirmation_email()