from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, TemplateView, FormView

from taggit.models import Tag

from .models import Article
from .forms import CommentForm, ArticleForm

	
class ArtileListView(ListView):
    paginate_by = 1
    template_name = 'blog/article_list/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
    	if 'tag_slug' in self.kwargs:
    		tag_slug = self.kwargs['tag_slug']
    		self.tag = get_object_or_404(Tag, slug=tag_slug)
    		articles = Article.was_published.filter(tags__in=[self.tag])

    	else:
    		self.tag = None
    		articles = Article.was_published.all()

    	return articles

    def get_context_data(self, **kwargs):
	    data = super().get_context_data(**kwargs)

	    data['tag'] = self.tag
	    return data


class ArticleView(TemplateView):
	template_name = 'blog/article_page/index.html'

	def get_context_data(self, **kwargs):
		article = get_object_or_404(Article, status='published', slug=kwargs["article_slug"])

		article_tags_ids = article.tags.values_list('id', flat=True)
		similar_articles = Article.was_published.filter(tags__in=article_tags_ids).exclude(id=article.id)

		comments = article.comments.filter(active=True)
		comment_form = CommentForm()

		context = {
			'article': article,
			'comments': comments,
			'comment_form': comment_form,
			'similar_articles': similar_articles[:4]
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


class ArticleCreateView(FormView):
	template_name = 'blog/article_create_page/index.html'
	form_class = ArticleForm

	def form_valid(self, form):
		article = form.save(commit=False)
		article.author = self.request.user
		article.save()
		return redirect(article.get_absolute_url())
	
