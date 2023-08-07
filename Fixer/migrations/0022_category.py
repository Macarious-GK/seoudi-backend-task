# Generated by Django 4.2.3 on 2023-07-21 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fixer', '0021_remove_items_category_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('countatni', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
