# Generated by Django 4.0.1 on 2022-05-29 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_tag_product_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='tag',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=b'I01\n', on_delete=django.db.models.deletion.DO_NOTHING, to='product.brand'),
        ),
    ]
