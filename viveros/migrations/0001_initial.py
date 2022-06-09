# Generated by Django 4.0.3 on 2022-06-09 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vivero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('provincia', models.CharField(max_length=40)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenesViveros')),
                ('localidad', models.CharField(max_length=40)),
                ('calle', models.CharField(max_length=40)),
                ('altura', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
                ('stockPlantas', models.CharField(max_length=2000)),
                ('stockProductos', models.CharField(max_length=2000)),
            ],
        ),
    ]
