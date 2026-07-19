from django.db import models
from django.conf import settings
from apps.administration.models import TimeStampedModel

class Doctor(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctor_profile', null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=200, db_index=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    bio = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"

class Service(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

class Blog(TimeStampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

class Gallery(TimeStampedModel):
    image_url = models.URLField()
    caption = models.CharField(max_length=255, blank=True, null=True)

class Testimonial(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(default=5)

class ContactInquiry(TimeStampedModel):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
