# Generated by Django 4.1.2 on 2022-10-18 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_news_options_news_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=True, max_length=150, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default=True, max_length=150, verbose_name='URL'),
        ),
    ]
