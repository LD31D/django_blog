from django import forms
from django.utils.text import slugify 

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

    def clean(self):
        data = super(ArticleForm, self).clean()
        title = data.get('title')
        slug = slugify(title)

        if Article.objects.filter(slug=slug).exists():
            raise forms.ValidationError('Article with this title already exists')

        return data

    class Meta:
        model = Article
        fields = ('title', 'tags', 'body', 'status')
        labels = {
            'body': 'Article body '
        }
        widgets = {
            'body': TextareaWidget(),
        }


class ArticleUpdateForm(forms.ModelForm):

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
