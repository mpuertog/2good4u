# Generated by Django 2.2 on 2019-09-28 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('ciudad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('entidad', models.CharField(max_length=100)),
                ('estatus', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('numero_cedula', models.IntegerField()),
                ('correo', models.CharField(max_length=100)),
                ('numero_telefono', models.IntegerField()),
                ('url_foto', models.CharField(blank=True, max_length=1000)),
                ('esAbogado', models.BooleanField(default=False)),
                ('descripcion_perfil', models.TextField(blank=True)),
                ('estudios', models.ManyToManyField(blank=True, to='asesorappConfig.Estudio')),
            ],
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField(blank=True)),
                ('tarifa_hora', models.IntegerField(default=0)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asesorappConfig.Usuario')),
                ('caso', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='asesorappConfig.Caso')),
            ],
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('texto', models.TextField()),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asesorappConfig.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='caso',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asesorappConfig.Usuario'),
        ),
    ]