from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	image = models.ImageField(upload_to='images/', null=True, blank=True)
	bio = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.user.username


def create_user_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_user_profile, sender=User)
