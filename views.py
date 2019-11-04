from django.shortcuts import render
from .models import Article, Writer
from .forms import ArticleForm, WriterForm
from django.http import JsonResponse
from datetime import datetime
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import CreateView

def homepage(request):
    return render(request, 'base.html',{
        'article_list' : Article.objects.all(),
    })

def articles_json(request):
    return JsonResponse({
        'items' : list(Article.objects.values()),
    })

def writers_json(request):
    return JsonResponse({
        'writersList' : list(Writer.objects.values()),
    })

def new_article(request):
    article_title = request.POST['article-headers'] #What the user inputs
    writerName = request.POST['writer-name']
    writerValue = Writer(id='1')
    article = Article(title=article_title, writer=writerValue)
    article.save()
    return JsonResponse({
        'id' : article.id,
        'title' : article.title
    })

# class ArticleCreateView(CreateView):
#     model = Article
#     fields = [
#         'title',
#         'body',
#     ]
# Create your views here.
