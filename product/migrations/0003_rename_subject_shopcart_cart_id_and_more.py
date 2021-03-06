# Generated by Django 4.0.1 on 2022-05-12 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_shopcart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopcart',
            old_name='subject',
            new_name='cart_id',
        ),
        migrations.RemoveField(
            model_name='shopcart',
            name='email',
        ),
        migrations.RemoveField(
            model_name='shopcart',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='shopcart',
            name='message',
        ),
        migrations.AddField(
            model_name='shopcart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='shopcart',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
