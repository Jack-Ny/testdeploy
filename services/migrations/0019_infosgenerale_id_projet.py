# Generated by Django 5.0.3 on 2024-05-04 04:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_infosgenerale'),
    ]

    operations = [
        migrations.AddField(
            model_name='infosgenerale',
            name='id_projet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='infos_generale', to='services.projet'),
        ),
    ]
