# Generated by Django 4.0.1 on 2022-05-22 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_subject_shopcart_cart_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='quantity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Quantities', to='product.quantity'),
        ),
    ]
