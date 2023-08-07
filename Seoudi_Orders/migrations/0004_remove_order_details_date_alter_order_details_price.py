# Generated by Django 4.2.4 on 2023-08-06 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seoudi_Orders', '0003_order_details_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_details',
            name='Date',
        ),
        migrations.AlterField(
            model_name='order_details',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
