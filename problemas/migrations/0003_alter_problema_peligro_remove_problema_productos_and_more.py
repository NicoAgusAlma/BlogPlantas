# Generated by Django 4.0.3 on 2022-06-11 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_producto_puntodeventa'),
        ('problemas', '0002_alter_problema_productos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problema',
            name='peligro',
            field=models.CharField(help_text='<br>Bajo, Medio o Alto', max_length=10),
        ),
        migrations.RemoveField(
            model_name='problema',
            name='productos',
        ),
        migrations.AddField(
            model_name='problema',
            name='productos',
            field=models.ManyToManyField(help_text='<br> Mantenga CTRL para seleccionar varios', to='productos.producto'),
        ),
        migrations.AlterField(
            model_name='problema',
            name='solucion',
            field=models.CharField(help_text='<br>Manera de solucionarlo', max_length=2000),
        ),
    ]
