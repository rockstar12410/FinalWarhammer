# Generated by Django 2.2 on 2023-12-13 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warhammer', '0003_remove_usedbuy_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newbuy',
            name='image',
            field=models.CharField(max_length=500),
        ),
    ]
