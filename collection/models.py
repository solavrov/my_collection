from django.db import models
from django.utils import timezone
from sorl.thumbnail import ImageField


class Item(models.Model):
    post_date = models.DateTimeField('Время добавления', default=timezone.now())
    name = models.CharField('Название', max_length=50)
    key_words = models.CharField('Ключевые слова', max_length=50, default='---')
    info = models.CharField('Комментарии', max_length=1000, default='---')
    photo = ImageField('Фото', upload_to='photos', default='no_image.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
