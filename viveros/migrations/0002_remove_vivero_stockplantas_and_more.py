# Generated by Django 4.0.3 on 2022-06-11 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viveros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vivero',
            name='stockPlantas',
        ),
        migrations.RemoveField(
            model_name='vivero',
            name='stockProductos',
        ),
    ]