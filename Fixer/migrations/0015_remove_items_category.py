# Generated by Django 4.2.3 on 2023-07-21 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fixer', '0014_category_items_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='category',
        ),
    ]
