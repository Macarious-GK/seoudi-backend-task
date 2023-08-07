# Generated by Django 4.2.3 on 2023-07-21 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fixer', '0015_remove_items_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Fixer.category'),
        ),
    ]
