from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):
    template_name = 'articles/news.html'
    ordering = 'published_at'
    articles = Article.objects.order_by(ordering).select_related('genre').select_related('author').\
        defer('published_at','author__phone')

    object_list = []
    for a in articles:
        object_list.append({
            'author': a.author.name,
            'genre': a.genre.name,
            'title': a.title,
            'text': a.text,
            'image': a.image,
        })

    context = {'object_list': object_list}
    return render(request, template_name, context)