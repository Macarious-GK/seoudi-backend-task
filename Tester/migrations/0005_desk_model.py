# Generated by Django 4.2.3 on 2023-07-22 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tester', '0004_romes_model_api'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desk_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255)),
                ('Color', models.CharField(max_length=255)),
            ],
        ),
    ]