# Generated by Django 4.0.3 on 2022-05-01 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título del proyecto')),
                ('description', models.TextField(max_length=200, verbose_name='Descripción del proyecto')),
                ('image', models.ImageField(upload_to='portfolios/', verbose_name='Imagen del proyecto')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación del proyecto')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización del proyecto')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
    ]
