from django.db import models


class Impress(models.Model):
    """Модель описывающая впечатление"""
    name = models.CharField(max_length=255, null=False, verbose_name="Название воспоминания")
    info = models.TextField(null=True, verbose_name="Инофрмация о воспоминании")
    date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Время')
