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


class Blog(models.Model):
    """Модель блоговой записи"""
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.CharField(max_length=100, verbose_name='slug')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(verbose_name='Изображение', upload_to='blog_image', blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(verbose_name='Опубликовано')
    view_count = models.IntegerField(verbose_name='Количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Version(models.Model):
    product = models.ForeignKey(Product, related_name='versions', on_delete=models.CASCADE, blank=True, null=True,
                                verbose_name='Товар')
    number = models.CharField(max_length=10, verbose_name='номер версии')
    name = models.CharField(max_length=100, verbose_name='название версии')
    is_active = models.BooleanField(verbose_name='признак текущей версии')

    def __str__(self):
        return f"{self.name}: {self.number}"

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
