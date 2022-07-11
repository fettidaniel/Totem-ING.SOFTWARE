# Generated by Django 4.0.5 on 2022-07-10 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_cliente_nombre_remove_cliente_rut_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='id',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='calificacion',
        ),
        migrations.AddField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(default='Hola', max_length=30, verbose_name='Nombre'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='rut',
            field=models.CharField(default='Hola', max_length=15, primary_key=True, serialize=False, verbose_name='Rut'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='asiento',
            field=models.IntegerField(default='1', verbose_name='Asientos disponibles'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='hora',
            field=models.CharField(default='Hola', max_length=5, verbose_name='Hora salida'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='numero',
            field=models.IntegerField(default='1', verbose_name='Numero de transfer'),
        ),
    ]