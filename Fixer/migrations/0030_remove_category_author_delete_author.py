# Generated by Django 4.2.3 on 2023-07-21 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fixer', '0029_category_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
