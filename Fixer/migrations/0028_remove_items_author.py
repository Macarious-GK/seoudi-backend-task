# Generated by Django 4.2.3 on 2023-07-21 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fixer', '0027_remove_category_author_items_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='author',
        ),
    ]
