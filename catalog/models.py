from django.db import models

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
    last_modified_date = models.DateField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
