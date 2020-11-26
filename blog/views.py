from django.shortcuts import get_object_or_404, render 
from django.views.generic import ListView, View

from .models import Article


class ArtileListView(ListView):
    queryset = Article.was_published.all()
    context_object_name = 'articles'
    template_name = 'blog/article_list/index.html'


class ArticleView(View):
	def get(self, request, slug):
		article = get_object_or_404(Article, status='published', slug=slug)
		context = {'article': article}
		return render(request, 'blog/article_page/index.html', context=context)
