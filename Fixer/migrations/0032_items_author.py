# Generated by Django 4.2.3 on 2023-07-21 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fixer', '0031_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Fixer.author'),
        ),
    ]
