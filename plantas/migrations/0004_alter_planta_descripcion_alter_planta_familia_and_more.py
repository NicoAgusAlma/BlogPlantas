# Generated by Django 4.0.3 on 2022-06-11 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problemas', '0002_alter_problema_productos'),
        ('plantas', '0003_alter_planta_viveros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planta',
            name='descripcion',
            field=models.CharField(help_text='<br> Descripcion de la planta.', max_length=3000),
        ),
        migrations.AlterField(
            model_name='planta',
            name='familia',
            field=models.CharField(help_text='<br> Arbol, planta, flor, cactacea, etc.', max_length=50),
        ),
        migrations.AlterField(
            model_name='planta',
            name='frecuenciaRiego',
            field=models.IntegerField(help_text='<br> Riegos mensuales.'),
        ),
        migrations.AlterField(
            model_name='planta',
            name='interior',
            field=models.BooleanField(default=True, verbose_name='Es planta de interior?'),
        ),
        migrations.AlterField(
            model_name='planta',
            name='luzDirecta',
            field=models.BooleanField(default=False, verbose_name='Luz solar directa?'),
        ),
        migrations.RemoveField(
            model_name='planta',
            name='peligrosComunes',
        ),
        migrations.AddField(
            model_name='planta',
            name='peligrosComunes',
            field=models.ManyToManyField(help_text='<br> Mantenga CTRL para seleccionar varios', to='problemas.problema'),
        ),
        migrations.AlterField(
            model_name='planta',
            name='precio',
            field=models.IntegerField(help_text='<br> Precio en U$s blue.'),
        ),
        migrations.AlterField(
            model_name='planta',
            name='sustrato',
            field=models.CharField(help_text='<br> Algun tipo de tierra especial?', max_length=50),
        ),
    ]
