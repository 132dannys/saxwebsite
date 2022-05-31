from distutils.command.upload import upload
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=200)
    image = models.ImageField('Изображение', upload_to='images/',  null=True, blank=True)
    video = models.FileField('Видео', upload_to='files/', null=True, blank=True)
    anons = models.CharField('Анонс', max_length=200)
    text = models.TextField('Статья')
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        pass

    def __str__(self) -> str:
        pass

    def get_absolute_url(self):
        pass
    