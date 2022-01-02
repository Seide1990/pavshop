# Generated by Django 4.0 on 2022-01-02 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_town_remove_countries_city_user_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, default='Baki', max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, default='Azerbaidjan', max_length=127, null=True),
        ),
        migrations.DeleteModel(
            name='Countries',
        ),
        migrations.DeleteModel(
            name='Town',
        ),
    ]