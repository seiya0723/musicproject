# Generated by Django 3.2 on 2022-11-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_countrycode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='introduction',
            field=models.TextField(blank=True, verbose_name='introduction'),
        ),
    ]
