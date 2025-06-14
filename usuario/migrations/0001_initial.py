# Generated by Django 5.2.1 on 2025-05-19 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescripcionRol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreRol', models.CharField(max_length=100)),
                ('descripcionRol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.DescripcionRol')),
                ('reportes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.reportes')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('documento', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('rol', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.rol')),
            ],
        ),
    ]
