from django import forms

from .models import Comment
from .widgets import CommentWidget

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body', )
        labels = {
        	'body': 'Your Comment: '
        }
        widgets = {
        	'body': CommentWidget()
        }

    class Media:
    	js = (
    		'https://code.jquery.com/jquery-3.5.1.min.js',
    		'https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js',
    		'https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote.min.js'
    	)

    	css = {
    		'screen': (
    				'https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote.min.css',
    				'https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css'
    			)
    	}


class CommentAdmin(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'body': CommentWidget(),
        }
