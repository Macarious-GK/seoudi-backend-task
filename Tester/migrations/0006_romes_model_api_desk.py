# Generated by Django 4.2.3 on 2023-07-22 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tester', '0005_desk_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='romes_model_api',
            name='Desk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Tester.desk_model'),
        ),
    ]
