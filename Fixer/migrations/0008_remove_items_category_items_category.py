# Generated by Django 4.2.3 on 2023-07-21 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fixer', '0007_delete_orderiter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='Category',
        ),
        migrations.AddField(
            model_name='items',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Fixer.category'),
        ),
    ]
