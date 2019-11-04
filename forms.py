from django import forms
from .models import Article, Writer

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'body',
            'writer'
        ]

class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = [
            'name'
        ]
