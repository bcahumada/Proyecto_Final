# Generated by Django 5.1.3 on 2024-11-20 20:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inmuebles', '0005_perfilusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comunas', to='Inmuebles.region'),
        ),
    ]
