# Generated by Django 4.0.3 on 2022-06-09 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreComun', models.CharField(max_length=40)),
                ('nombreCientifico', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenesPlantas')),
                ('familia', models.CharField(help_text='Arbol, planta, flor, cactacea, etc.', max_length=50)),
                ('sustrato', models.CharField(help_text='Algun tipo de tierra especial?', max_length=50)),
                ('precio', models.IntegerField(help_text='Precio en U$s blue.')),
                ('viveros', models.CharField(help_text='Viveros donde encontrarla.', max_length=100)),
                ('peligrosComunes', models.CharField(help_text='Problemas más usuales.', max_length=100)),
                ('interior', models.BooleanField(default=True, verbose_name='interior')),
                ('luzDirecta', models.BooleanField(default=False, help_text='Necesita luz solar directa?.')),
                ('frecuenciaRiego', models.IntegerField(help_text='Riegos mensuales.')),
                ('descripcion', models.CharField(help_text='Descripcion de la planta.', max_length=3000)),
            ],
        ),
    ]
