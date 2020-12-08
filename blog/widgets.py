from django.forms.widgets import Textarea


class TextareaWidget(Textarea):

    template_name = 'widgets/textarea.html'

    class Media:
        js = (
            "https://code.jquery.com/jquery-3.4.1.min.js",
            "https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js",
            "https://cdn.jsdelivr.net/npm/summernote@0.8.15/dist/summernote.min.js"
        )

        css = {
            'screen': (
                "https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css",
                "https://cdn.jsdelivr.net/npm/summernote@0.8.15/dist/summernote.min.css"
            )
        }
        