# Generated by Django 4.0.3 on 2022-06-10 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='posteo',
            name='tags',
        ),
        migrations.AlterField(
            model_name='posteo',
            name='texto',
            field=models.TextField(max_length=5000),
        ),
    ]