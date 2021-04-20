# Generated by Django 3.2 on 2021-04-20 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Impress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название воспоминания')),
                ('info', models.TextField(null=True, verbose_name='Инофрмация о воспоминании')),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Время')),
            ],
        ),
    ]
