# Generated by Django 3.0.4 on 2020-04-02 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0004_catalog_catalogcase_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='name',
            field=models.CharField(help_text='Catalog Name', max_length=200),
        ),
    ]
