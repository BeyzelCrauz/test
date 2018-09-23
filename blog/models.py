from django.db import models
from django.utils import timezone


class Post (models.Model):
    identif = models.IntegerField(default=0, verbose_name='Идентификатор (Уникальный!!!)')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    short_text = models.TextField(max_length=200, default='', verbose_name='короткий текст, в превью статьи')
    text = models.TextField(verbose_name='весь текст')
    img = models.ImageField(upload_to='media/', blank=True, verbose_name='Картинка в блоге. Обязательно.')
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.title


class Flat (models.Model):
    idef = models.IntegerField(default=0, verbose_name='Идентификатор (Уникальный!!!)')
    type_Flat_Land = models.CharField(max_length=200, default="flat", verbose_name='Участок или земля flat или land')
    subtype_Rent_Sale = models.CharField(max_length=200, default="rent", verbose_name='Продажа или аренда rent или sale')
    district = models.CharField(max_length=200, default="0", verbose_name='Район (без ошибок, а то не сработает)')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.CharField(max_length=5200, verbose_name='Описание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    bank_price = models.IntegerField(default=0, verbose_name='Цена в ипотеку')
    adres = models.CharField(max_length=200, default='', verbose_name='Адрес')
    room = models.IntegerField(default=0, verbose_name='Количество комнат')
    square = models.IntegerField(default=0, verbose_name='Площадь')
    live_square = models.IntegerField(default=0, verbose_name='Общая площадь')
    kitchen_square = models.IntegerField(default=0, verbose_name='Площадь кухни')
    price_for_square = models.IntegerField(default=0, verbose_name='Цена за квадрат')
    floor = models.IntegerField(default=0, verbose_name='Этаж')
    floors = models.IntegerField(default=0, verbose_name='Колличество этажей')
    year = models.IntegerField(default=0, verbose_name='Год постройки')
    house_type = models.CharField(max_length=200, default='' , verbose_name='Тип дома')
    house_material = models.CharField(max_length=200, default='', verbose_name='Материал дома')
    seller_name = models.CharField(max_length=200, default='', verbose_name='Имя продавца')
    seller_phone = models.CharField(max_length=200, default='', verbose_name='Номер продавца')
    img = models.ImageField(upload_to='media/', blank=True, verbose_name='Картинка в превью. Обязательно.')
