# Generated by Django 4.0.5 on 2022-11-07 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_pimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pimage',
            field=models.ImageField(upload_to='upload'),
        ),
    ]
