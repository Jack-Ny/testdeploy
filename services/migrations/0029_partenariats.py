# Generated by Django 5.0.3 on 2024-05-14 12:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0028_remove_activiteplu_budget_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partenariats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True)),
                ('numero', models.CharField(max_length=100, null=True)),
                ('date_debut', models.CharField(max_length=50, null=True)),
                ('date_fin', models.CharField(max_length=50, null=True)),
                ('id_general', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_general_part', to='services.infosgenerale')),
            ],
        ),
    ]
