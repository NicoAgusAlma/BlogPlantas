# Generated by Django 4.0.3 on 2022-06-11 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viveros', '0002_remove_vivero_stockplantas_and_more'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='puntoDeVenta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viveros.vivero'),
        ),
    ]