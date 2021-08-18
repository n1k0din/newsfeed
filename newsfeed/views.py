from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from news.models import NewsPost


def index(request):
    news = NewsPost.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(news, 1)

    try:
        news_on_page = paginator.page(page)
    except PageNotAnInteger:
        news_on_page = paginator.page(1)
    except EmptyPage:
        news_on_page = paginator.page(paginator.num_pages)

    dumped_news = []
    for news_post in news_on_page:
        dumped_news_post = {
            'title': news_post.title,
            'text': news_post.text,
            'imgs': [photo.image.url for photo in news_post.news_post_photos.all()] or None,
            'published_at': news_post.published_at,
        }
        dumped_news.append(dumped_news_post)

    context = {'news': dumped_news, 'paginator': news_on_page}

    return render(request, 'index.html', context)
