# Generated by Django 5.0.7 on 2025-01-22 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sold_car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('year', models.PositiveSmallIntegerField()),
                ('hususiyat', models.CharField(max_length=30)),
                ('km', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
