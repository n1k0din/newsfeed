from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from news.models import NewsPost


def index(request):
    news = NewsPost.objects.all()

    correct_per_page_params = (10, 20, 50)
    default_news_per_page, *_ = correct_per_page_params

    user_news_per_page = request.GET.get('per_page', default_news_per_page)
    try:
        news_per_page = int(user_news_per_page)
    except ValueError:
        news_per_page = default_news_per_page

    if news_per_page not in correct_per_page_params:
        news_per_page = default_news_per_page

    page = request.GET.get('page', 1)

    print(f'{user_news_per_page=} {news_per_page=}')

    paginator = Paginator(news, news_per_page)

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

    context = {
        'news': dumped_news,
        'paginator': news_on_page,
        'per_page': news_per_page,
        'per_page_params': correct_per_page_params,
    }

    return render(request, 'index.html', context)
