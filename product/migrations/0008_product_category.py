# Generated by Django 4.0.1 on 2022-05-29 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Category',
            field=models.ForeignKey(null=b'I01\n', on_delete=django.db.models.deletion.DO_NOTHING, to='product.category'),
            preserve_default=b'I01\n',
        ),
    ]