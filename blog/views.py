from django.views.generic import ListView

from .models import Article

class ArtileListView(ListView):
    queryset = Article.was_published.all()
    context_object_name = 'articles'
    template_name = 'blog/article_list/index.html'
