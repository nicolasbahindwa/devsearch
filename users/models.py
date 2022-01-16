from django.db import models
from django.contrib.auth.models import User
from utils.utils_db import TimeStamps
import uuid
# Create your models here.


class Profile(TimeStamps, models.Model):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500,
                              unique=True, blank=True, null=True)
    username = models.CharField(max_length=200,
                                unique=True, blank=True, null=True)
    location = models.CharField(max_length=200,
                                unique=True, blank=True, null=True)
    short_intro = models.CharField(max_length=300, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/',
        default='profiles/user-default.png')
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4,
                          unique=True,
                          primary_key=True,
                          editable=False)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ['-create_at']

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except Exception:
            url = '/images/default.jpg'
        return url


class Skill(TimeStamps, models.Model):
    owner = models.ForeignKey(Profile,
                              on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4,
                          unique=True,
                          primary_key=True,
                          editable=False)

    def __str__(self):
        return str(self.name)


class Message(TimeStamps, models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(
        Profile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="messages")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    id = models.UUIDField(default=uuid.uuid4,
                          unique=True,
                          primary_key=True,
                          editable=False)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-create_at']
