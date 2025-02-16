# Generated by Django 5.0.6 on 2024-06-26 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0002_productos_delete_registropiezas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('cantidad', models.IntegerField(default=1)),
                ('image', models.ImageField(blank=True, upload_to='productos')),
            ],
        ),
    ]
