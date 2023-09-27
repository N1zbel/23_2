from django.core.management import BaseCommand
from user_app.models import User


class Command(BaseCommand):
    help = 'создание суперпользователя'

    def handle(self, *args, **options):
        user = User.objects.create(
            email='nizbel@inbox.ru',
            first_name='Admin',
            last_name='Admin',
            is_superuser=True,
            is_staff=True
        )

        user.set_password('password')
        user.save()
