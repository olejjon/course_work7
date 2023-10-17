from django.core.management import BaseCommand
from users.models import Users


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = Users.objects.create(
            email="admin@gmail.com",
            first_name="admin@gmail.com",
            last_name="admin@gmail.com",
            telegram_user_name="admin",
            is_superuser=True,
            is_staff=True,
            is_active=True
            )

        user.set_password("admin")
        user.save()
