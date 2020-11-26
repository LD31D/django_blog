from django.urls import path

from .views import *

urlpatterns = [
    path('', ArtileListView.as_view()),
    path('<str:slug>/', ArticleView.as_view()),
]
