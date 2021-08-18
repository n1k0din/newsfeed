from django.shortcuts import render

from news.models import NewsPost


def index(request):
    news = NewsPost.objects.all()

    dumped_news = []
    for news_post in news:
        dumped_news_post = {
            'title': news_post.title,
            'text': news_post.text,
            'imgs': [photo.image.url for photo in news_post.news_post_photos.all()] or None,
            'published_at': news_post.published_at,
        }
        dumped_news.append(dumped_news_post)

    context = {'news': dumped_news}

    return render(request, 'index.html', context)
