from django.shortcuts import get_object_or_404, render 
from django.views.generic import ListView, TemplateView

from taggit.models import Tag

from .models import Article
from .forms import CommentForm

	
class ArtileListView(ListView):
    paginate_by = 1
    template_name = 'blog/article_list/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
    	if 'tag_slug' in self.kwargs:
    		tag_slug = self.kwargs['tag_slug']
    		tag = get_object_or_404(Tag, slug=tag_slug)
    		articles = Article.was_published.filter(tags__in=[tag])

    	else:
    		articles = Article.was_published.all()

    	return articles


class ArticleView(TemplateView):
	template_name = 'blog/article_page/index.html'

	def get_context_data(self, **kwargs):
		article = get_object_or_404(Article, status='published', slug=kwargs["article_slug"])
		comments = article.comments.filter(active=True)
		comment_form = CommentForm()

		context = {
			'article': article,
			'comments': comments,
			'comment_form': comment_form
			}
		return context

	def post(self, request, **kwargs):
		context = self.get_context_data(**kwargs)

		comment_form = CommentForm(data=request.POST)

		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)

			new_comment.article = context['article']
			new_comment.author = request.user

			new_comment.save()

		return render(request, self.template_name, context=context)
