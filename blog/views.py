from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, TemplateView, FormView

from taggit.models import Tag

from .models import Article
from .forms import CommentForm, ArticleForm, ArticleValidateForm

	
class ArtileListView(ListView):
    paginate_by = 5
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

    	self.query = self.request.GET.get('q', '')
    	if self.query:
    		articles = articles.filter(Q(title__icontains=self.query) | Q(body__icontains=self.query))

    	return articles

    def get_context_data(self, **kwargs):
	    data = super().get_context_data(**kwargs)

	    data['tag'] = self.tag
	    data['query'] = self.query
	    data['most_common_tags'] = Article.tags.most_common()[:5]
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


class ArticleCreateView(LoginRequiredMixin, FormView):
	template_name = 'blog/article_create_page/index.html'
	form_class = ArticleValidateForm
	login_url = '/accounts/login/'

	def form_valid(self, form):
		article = form.save(commit=False)
		article.author = self.request.user
		article.save()

		if article.status == 'published':
			return redirect(article.get_absolute_url())
		else:
			return redirect('/blog/')


class ArticleEditView(LoginRequiredMixin, UpdateView):
	template_name = 'blog/article_edit_page/index.html'
	form_class = ArticleForm

	def get_success_url(self):
		if self.article.status == 'published':
			return self.article.get_absolute_url()
		else:
			return '/blog/'

	def get_object(self, queryset=None):
		self.article = get_object_or_404(Article, author=self.request.user, slug=self.kwargs.get("article_slug"))
		return self.article


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
	template_name = 'blog/article_edit_page/article_confirm_delete.html'
	model = Article
	success_url = '/blog/'

	def get_success_url(self):
		return self.success_url

	def get_object(self, queryset=None):
		article = get_object_or_404(Article, author=self.request.user, slug=self.kwargs.get("article_slug"))
		return article
