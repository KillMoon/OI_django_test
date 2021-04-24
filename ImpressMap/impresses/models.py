from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """Модель описывающая профиль пользователя"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=255, null=False, verbose_name="Ссылка на аватар")

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Impress(models.Model):
    """Модель описывающая впечатление"""
    name = models.CharField(max_length=255, null=False, verbose_name="Название воспоминания")
    info = models.TextField(null=True, verbose_name="Инофрмация о воспоминании")
    date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Время')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Автор", blank=True, null=True)
