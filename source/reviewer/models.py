from django.db import models
from django.contrib.auth.models import User

DEFAULT_CATEGORY = 'other'
CATEGORY_CHOICES = [(DEFAULT_CATEGORY, 'Разное'), ('Food', 'Еда'), ('Toys', 'Игрушки'), ('Tools', 'Инструменты')]

class Product(models.Model):
    product_name = models.CharField(max_length=10, null=False, blank=False, verbose_name='Название товара')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=DEFAULT_CATEGORY, null=False, blank=False, verbose_name='Категория товара')
    description = models.TextField(max_length=100, null=True, blank=True, verbose_name='Описание товара')

    def __str__(self):
        return '{}. {}. {}'.format(self.pk, self.product_name, self.category)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1, related_name='reviews', verbose_name='Автор')
    product = models.ForeignKey('reviewer.Product', on_delete=models.CASCADE, related_name='products', verbose_name='Товар')
    review_text = models.TextField(max_length=200, null=False, blank=False, verbose_name='Текст отзыва')

    def __str__(self):
        return '{}. {}'.format(self.pk, self.product)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'