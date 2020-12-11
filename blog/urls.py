from django.urls import path

from .views import *


urlpatterns = [
    path('', ArtileListView.as_view(), name='index'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('<article_slug>/', ArticleView.as_view(), name='article_view'),
    path('<article_slug>/edit/', ArticleEditView.as_view(), name='article_edit'),
    path('<article_slug>/edit/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('tag/<tag_slug>/', ArtileListView.as_view(), name='tag_view'),
]
