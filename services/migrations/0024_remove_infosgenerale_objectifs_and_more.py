# Generated by Django 5.0.3 on 2024-05-06 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0023_objectif'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infosgenerale',
            name='objectifs',
        ),
        migrations.AddField(
            model_name='infosgenerale',
            name='autre_groupe',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
