from django.contrib import admin

from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'published', 'status')
	list_filter = ('status', 'created', 'published', 'author')
	list_editable = ('status',)
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('author',)
	date_hierarchy = 'published'
	ordering = ['status', 'published']
