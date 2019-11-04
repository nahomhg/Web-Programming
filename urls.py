"""WebProgLab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from newsArticles.views import homepage, articles_json, new_article, writers_json

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', homepage, name="homepage"),
    #path('create/', createArticleForm, name="create"),
    path('articles.json/', articles_json, name="list of articles"),
    path('new_article/', new_article, name="new article"),
    path('writers_json/', writers_json, name="writer names"),
]
