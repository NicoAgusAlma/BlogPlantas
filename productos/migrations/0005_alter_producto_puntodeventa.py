# Generated by Django 4.0.3 on 2022-06-11 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viveros', '0002_remove_vivero_stockplantas_and_more'),
        ('productos', '0004_remove_producto_puntodeventa_producto_puntodeventa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='puntoDeVenta',
            field=models.ManyToManyField(blank=True, help_text='<br> Mantenga CTRL para seleccionar varios', null=True, to='viveros.vivero'),
        ),
    ]
