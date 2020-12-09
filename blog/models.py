from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify 
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

from .managers import WasPublishedManager


class Article(models.Model):
	objects = models.Manager()
	was_published = WasPublishedManager()

	STATUS_CHOICES = (
			('draft', 'Draft'),
			('published', 'Published')
		)

	title = models.CharField(max_length=256)
	slug = models.SlugField(max_length=256, unique=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
	tags = TaggableManager(blank=True)
	body = models.TextField()
	published = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	class Meta:
		ordering = ('-published',)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		return super(Article, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('blog:article_view', args=[self.slug])


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Comment by {self.author} on {self.article}'
