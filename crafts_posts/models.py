from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=225, unique=True, null=False, blank=False)
    content = models.TextField(max_length=2200, null=True, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_zzr2uj',
        null=False, blank=False
    )
    alt_text = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
    
    def clean(self):
        if not self.content and not self.image:
            raise ValidationError("At least one of 'content' or 'image' must be provided.")
