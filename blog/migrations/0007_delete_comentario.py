# Generated by Django 4.0.3 on 2022-06-12 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comentario_nombre'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]
