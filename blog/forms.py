from django import forms

from .models import Comment, Article
from .widgets import TextareaWidget


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body', )
        labels = {
        	'body': 'Your Comment: '
        }
        widgets = {
        	'body': TextareaWidget()
        }



class CommentAdmin(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'body': TextareaWidget(),
        }


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'tags', 'body', 'status')
        labels = {
            'body': 'Article body '
        }
        widgets = {
            'body': TextareaWidget(),
        }


class ArticleAdmin(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'body': TextareaWidget(),
        }
