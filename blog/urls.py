from django.urls import path

from .views import *


urlpatterns = [
    path('', ArtileListView.as_view()),
    path('create/', ArticleCreateView.as_view(), name='article_add/'),
    path('<article_slug>/', ArticleView.as_view(), name='article_view'),
    path('tag/<tag_slug>/', ArtileListView.as_view(), name='tag_view'),
]
