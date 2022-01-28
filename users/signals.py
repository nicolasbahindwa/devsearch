from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings

# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )
        subject = 'Welcome to developer search'
        Message = 'Thanks for joining the team of developer world wide. we hope you enjoy coding with us.'

        send_mail(
            subject,
            Message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False
        )


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created is False:
        user._first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        # print(user + "============== ")
        user.delete()
    except Exception:
        pass


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)
post_save.connect(updateUser, sender=Profile)

