# Generated by Django 4.0.3 on 2022-06-09 03:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Posteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('subtitulo', models.CharField(max_length=100)),
                ('fecha', models.DateField(help_text='AAAA/MM/DD')),
                ('texto', models.CharField(max_length=5000)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenesPosteos')),
                ('categoria', models.CharField(default='', max_length=100)),
                ('tags', models.CharField(default='', max_length=100)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
