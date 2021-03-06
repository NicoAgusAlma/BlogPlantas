# Generated by Django 4.0.3 on 2022-06-11 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problemas', '0004_alter_problema_peligro_alter_problema_solucion'),
        ('viveros', '0002_remove_vivero_stockplantas_and_more'),
        ('plantas', '0006_alter_planta_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planta',
            name='peligrosComunes',
            field=models.ManyToManyField(blank=True, help_text='<br> Mantenga CTRL para seleccionar varios', null=True, to='problemas.problema'),
        ),
        migrations.AlterField(
            model_name='planta',
            name='viveros',
            field=models.ManyToManyField(blank=True, help_text='<br> Mantenga CTRL para seleccionar varios', null=True, to='viveros.vivero'),
        ),
    ]
