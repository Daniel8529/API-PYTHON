# Generated by Django 4.2.2 on 2023-07-03 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Fecha', models.CharField(max_length=50)),
                ('Tipo', models.CharField(max_length=60)),
                ('Image', models.CharField(max_length=500)),
                ('Ciudad', models.CharField(max_length=50)),
                ('Lugar', models.CharField(max_length=50)),
                ('Cantidad', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Secciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdEvento', models.CharField(max_length=100)),
                ('Tipo', models.CharField(max_length=60)),
                ('Secciones', models.CharField(max_length=60)),
                ('Is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('NombreUsuario', models.CharField(max_length=60)),
                ('Correo', models.CharField(max_length=90)),
                ('Password', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
