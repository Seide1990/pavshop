# Generated by Django 4.0.1 on 2022-03-08 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopcart',
            name='product',
        ),
        migrations.AddField(
            model_name='shopcart',
            name='name',
            field=models.CharField(default=1, max_length=155),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopcart',
            name='price',
            field=models.CharField(default='299$', max_length=155),
        ),
    ]