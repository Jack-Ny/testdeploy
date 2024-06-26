# Generated by Django 5.0.3 on 2024-05-07 10:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0026_projet_created'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infosgenerale',
            name='selected_collab',
        ),
        migrations.AddField(
            model_name='activite',
            name='utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activiteplu',
            name='utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activiteplus', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='infosgenerale',
            name='utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='generales', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projet',
            name='utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projets', to=settings.AUTH_USER_MODEL),
        ),
    ]
