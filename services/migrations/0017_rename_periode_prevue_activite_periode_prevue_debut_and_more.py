# Generated by Django 5.0.3 on 2024-04-30 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0016_alter_activite_unite_physique'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activite',
            old_name='periode_prevue',
            new_name='periode_prevue_debut',
        ),
        migrations.AddField(
            model_name='activite',
            name='budget_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='activite',
            name='periode_prevue_fin',
            field=models.CharField(max_length=50, null=True),
        ),
    ]