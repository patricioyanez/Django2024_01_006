# Generated by Django 4.2.1 on 2024-06-10 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido1', models.CharField(max_length=50)),
                ('apellido2', models.CharField(max_length=50)),
            ],
        ),
    ]
