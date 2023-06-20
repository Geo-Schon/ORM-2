from django.views.generic import ListView
from django.shortcuts import render
from .models import Article, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    context = {'articles': Article.objects.order_by(ordering).all()}
    # for article in context['articles']:
    #     all_article_scopes = ArticleScope.objects.filter(article__id=article[id])
    #     print(all_article_scopes)
    print(context)
    return render(request, template, context)
