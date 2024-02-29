from django.db import models


# Create your models here.
class Category(models.Model):
    """Класс для модели категория"""
    name = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание')  # varchar

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """Класс для модели продукта"""
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    description = models.TextField(verbose_name='Описание')  # varchar
    image = models.ImageField(verbose_name='Изображение', upload_to='product_image', blank=True, null=True, )
    category = models.ForeignKey(Category, related_name="products", on_delete=models.SET_NULL, blank=True, null=True,
                                 verbose_name='Категории')
    price = models.DecimalField(verbose_name='Розничная Цена', max_digits=10, decimal_places=2)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ContactDetails(models.Model):
    """Класс для модели контактных данных"""
    name = models.CharField(max_length=100, verbose_name='Имя')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    email = models.CharField(max_length=100, verbose_name='Адрес электронной почты')
    phone = models.CharField(max_length=100, verbose_name='Контактный телефон')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактные данные'
