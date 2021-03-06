# Generated by Django 4.0.1 on 2022-05-01 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_shopcart_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopcart',
            name='name',
        ),
        migrations.RemoveField(
            model_name='shopcart',
            name='price',
        ),
        migrations.RemoveField(
            model_name='shopcart',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='shopcart',
            name='user',
        ),
        migrations.AddField(
            model_name='shopcart',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shopcart',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shopcart',
            name='message',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopcart',
            name='subject',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
