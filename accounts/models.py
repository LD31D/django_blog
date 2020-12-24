from uuid import uuid4 

from django.db import models
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models.signals import post_save


User._meta.get_field('email')._unique = True


class EmailConfirm(models.Model):
	activate_code = models.SlugField(max_length=256, unique=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

	def save(self, *args, **kwargs):
		self.activate_code = str(uuid4())

		send_mail(
		    'Confirm Email',
		    f'{self.get_absolute_url()}',
		    'from@example.com',
		    [self.user.email],
		    fail_silently=False,
		)

		return super(EmailConfirm, self).save(*args, **kwargs)


	def get_absolute_url(self):
		return reverse('accounts:email_confirm', kwargs={'slug': self.activate_code})


def email_confirm(sender, **kwargs):
	if kwargs['created']:
		EmailConfirm.objects.create(user=kwargs['instance'])


post_save.connect(email_confirm, sender=User)
