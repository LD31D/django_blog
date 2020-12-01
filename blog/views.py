from django.shortcuts import get_object_or_404, render 
from django.views.generic import ListView, View

from .models import Article
from .forms import CommentForm

	
class ArtileListView(ListView):
    paginate_by = 1
    template_name = 'blog/article_list/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        articles = Article.was_published.all()

        return articles
        

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
		comment_form = CommentForm()

		context.update({'comment_form': comment_form})
		return render(request, 'blog/article_page/index.html', context=context)

	def post(self, request, slug):
		context = self.get_objects(slug)

		comment_form = CommentForm(data=request.POST)

		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)

			new_comment.article = context['article']
			new_comment.author = request.user

			new_comment.save()

		comment_form = CommentForm()
		context.update({'comment_form': comment_form})
		return render(request, 'blog/article_page/index.html', context=context)
