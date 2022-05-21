# Generated by Django 4.0.1 on 2022-05-01 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_remove_shopcart_product_remove_shopcart_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopcart',
            old_name='quantity',
            new_name='name',
        ),
        migrations.AddField(
            model_name='shopcart',
            name='price',
            field=models.CharField(default='299$', max_length=155),
        ),
    ]