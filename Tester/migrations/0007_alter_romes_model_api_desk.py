# Generated by Django 4.2.3 on 2023-07-22 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tester', '0006_romes_model_api_desk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='romes_model_api',
            name='Desk',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.PROTECT, to='Tester.desk_model'),
        ),
    ]
