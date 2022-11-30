# Generated by Django 3.2.6 on 2022-11-26 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название товара', max_length=200, verbose_name='Название товара')),
                ('price', models.PositiveIntegerField(help_text='Введите название товара', verbose_name='Цена товара')),
                ('description', models.CharField(help_text='Опишите товар', max_length=1000, null=True, verbose_name='Описание товара')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания объявления')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pictures/ad/', verbose_name='Обложка объявления')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to=settings.AUTH_USER_MODEL, verbose_name='Автор объявления')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Вы можете оставить комментарий', max_length=1000, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания комментария')),
                ('ad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_ad', to='ads.ad', verbose_name='Объявление, к которому относится комментарий')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ads.ad', verbose_name='Автор комментария')),
            ],
        ),
    ]
