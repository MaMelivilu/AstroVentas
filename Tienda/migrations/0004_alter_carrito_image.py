# Generated by Django 5.0.6 on 2024-06-26 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0003_carrito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='image',
            field=models.ImageField(blank=True, upload_to='carrito'),
        ),
    ]
