from django.shortcuts import get_object_or_404, render 
from django.views.generic import ListView, View

from .models import Article

	
class ArtileListView(ListView):
    queryset = Article.was_published.all()
    paginate_by = 1
    context_object_name = 'articles'
    template_name = 'blog/article_list/index.html'


class ArticleView(View):
	def get_objects(self, slug):
		article = get_object_or_404(Article, status='published', slug=slug)
		comments = article.comments.filter(active=True)

		context = {
			'article': article,
			'comments': comments
			}
		return context

	def get(self, request, slug):
		context = self.get_objects(slug)
		
		return render(request, 'blog/article_page/index.html', context=context)
