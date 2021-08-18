from django.db import models


class NewsPost(models.Model):
    title = models.CharField('Title', max_length=200)
    text = models.TextField('Full text')
    published_at = models.DateTimeField('Publication date and time')

    def __str__(self):
        return self.title


class Photo(models.Model):
    image = models.ImageField('Image', upload_to='images')
    sort_index = models.PositiveSmallIntegerField(
        'Sorting index',
        default=0,
        blank=True,
    )

    news_post = models.ForeignKey(
        NewsPost,
        related_name='news_post_photos',
        verbose_name='News post',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['sort_index']

    def __str__(self):
        return f'{self.sort_index} {self.news_post.title}'
