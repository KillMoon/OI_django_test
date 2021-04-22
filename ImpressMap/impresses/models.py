from django.contrib.auth.models import User
from django.db import models


class Impress(models.Model):
    """Модель описывающая впечатление"""
    name = models.CharField(max_length=255, null=False, verbose_name="Название воспоминания")
    info = models.TextField(null=True, verbose_name="Инофрмация о воспоминании")
    date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Время')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", blank=True, null=True)