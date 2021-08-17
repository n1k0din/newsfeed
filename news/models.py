from django.db import models


class NewsPost(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Полный текст')
    published_at = models.DateTimeField('Дата и время публикации')
    image = models.ImageField('Картинка', blank=True, upload_to='images')
