from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=60)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # страница на которую необходимо переадрессовывать пользователя после того как мы обновим или удалим запись
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

