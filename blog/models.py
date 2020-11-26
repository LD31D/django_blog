from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Article(models.Model):
	STATUS_CHOICES = (
			('draft', 'Draft'),
			('published', 'Published')
		)

	title = models.CharField(max_length=256)
	slug = models.SlugField(max_length=256, unique=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
	body = models.TextField()
	published = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	class Meta:
		ordering = ('-published',)

	def __str__(self):
		return self.title
