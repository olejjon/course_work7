from django.db import models
from django.contrib.auth.models import AbstractUser

from constants import NULLABLE


class Users(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="email")
    chat_id = models.IntegerField(unique=True, **NULLABLE, default=None)
    telegram_user_name = models.CharField(max_length=100, **NULLABLE, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "users"
        verbose_name_plural = 'users'
