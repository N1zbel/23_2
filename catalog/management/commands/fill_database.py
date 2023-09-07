from django.core.management.base import BaseCommand
from django.db import transaction
import json

from catalog.models import Product, Category
from skystore.settings import BASE_DIR


class Command(BaseCommand):
    '''
    Заполняет базу данных новыми данными и очищает старые данные
    '''

    def handle(self, *args, **kwargs):
        # Очистка базу данных от старых данных

        Product.objects.all().delete()
        Category.objects.all().delete()
        print('База данных успешно очищенна')

        # Заполнение базы данных новыми данными
        print('Заполнение базы данных новыми данными...')
        with transaction.atomic():
            with open(BASE_DIR / 'catalog/fixtures/categories_data.json', 'r', encoding='utf-8') as file:
                category_data = json.load(file)
                for category in category_data:
                    Category.objects.create(
                        pk=category['pk'],
                        name=category['fields']['name'],
                        description=category['fields']['description']
                    )
            with open(BASE_DIR / 'catalog/fixtures/product_data.json', 'r', encoding='utf-8') as file:
                product_data = json.load(file)
                for product in product_data:
                    category_pk = product['fields']['category']
                    category_instance = Category.objects.get(pk=category_pk)
                    Product.objects.create(
                        pk=product['pk'],
                        name=product['fields']['name'],
                        description=product['fields']['description'],
                        category=category_instance,
                        purchase_price=product['fields']['purchase_price'],
                        date_of_creation=product['fields']['date_of_creation'],
                        last_modified_date=product['fields']['last_modified_date'],
                    )

            print('База данных успешно заполнена новыми данными')
