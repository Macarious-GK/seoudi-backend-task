# Generated by Django 4.2.3 on 2023-07-21 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fixer', '0037_category_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='author',
        ),
    ]
