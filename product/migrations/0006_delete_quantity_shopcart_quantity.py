# Generated by Django 4.0.1 on 2022-05-22 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_shopcart_quantity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Quantity',
        ),
        migrations.AddField(
            model_name='shopcart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]