# Generated by Django 4.0.3 on 2022-06-11 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problemas', '0003_alter_problema_peligro_remove_problema_productos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problema',
            name='peligro',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='problema',
            name='solucion',
            field=models.TextField(help_text='<br>Manera de solucionarlo', max_length=2000),
        ),
    ]