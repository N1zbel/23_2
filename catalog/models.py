from django.db import models

from user_app.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание продукта')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название продукта')
    description = models.TextField(verbose_name='Описание продукта')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Ревью')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Название категории')
    purchase_price = models.IntegerField(verbose_name='Цена продукта')
    date_of_creation = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    last_modified_date = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')
    versions = models.ManyToManyField('catalog.Version', related_name='products', blank=True,
                                      verbose_name='Версии продукта')
    author = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,**NULLABLE, verbose_name='Продукт')
    version_num = models.FloatField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Название версии')
    is_active = models.BooleanField(default=True, verbose_name='Признак текущей версии')

    def __str__(self):
        return self.version_name

    class Meta:
        verbose_name = 'Версию'
        verbose_name_plural = 'Версии'
