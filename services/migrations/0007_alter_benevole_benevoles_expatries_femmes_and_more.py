# Generated by Django 5.0.3 on 2024-04-15 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_informationgenerale_boite_postale_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benevole',
            name='benevoles_expatries_femmes',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='benevole',
            name='benevoles_expatries_hommes',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='benevole',
            name='benevoles_expatries_total',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='benevole',
            name='benevoles_nationaux_femmes',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='benevole',
            name='benevoles_nationaux_hommes',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='benevole',
            name='benevoles_nationaux_total',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='gouvernanceinterne',
            name='designation',
            field=models.CharField(choices=[('renouvellement_instances', 'Dernier renouvellement des Instances dirigeantes'), ('assemblee_generale', 'Dernière Assemblée Générale Ordinaire'), ('session_bureau_executif', 'Dernière session statutaire du bureau exécutif'), ('mandat_bureau_executif', 'Durée du mandat du bureau exécutif')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='partenaire',
            name='ministere',
            field=models.CharField(choices=[('ministere1', 'Ministère 1'), ('ministere2', 'Ministère 2'), ('ministere3', 'Ministère 3')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='partenaire',
            name='protocole_entente_collectivite',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='partenaire',
            name='protocole_entente_convention',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personneladministration',
            name='personnel_admin_femme',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personneladministration',
            name='personnel_admin_homme',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personneladministration',
            name='personnel_admin_total',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personnelemploye',
            name='employes_expatries_cdd_femmes',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personnelemploye',
            name='employes_expatries_cdd_hommes',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personnelemploye',
            name='employes_expatries_cdd_total',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personnelemploye',
            name='employes_expatries_cdi_femmes',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personnelemploye',
            name='employes_expatries_cdi_hommes',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personnelemploye',
            name='employes_expatries_cdi_total',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personnelemploye',
            name='employes_nationaux_cdd_femmes',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personnelemploye',
            name='employes_nationaux_cdd_hommes',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personnelemploye',
            name='employes_nationaux_cdd_total',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personnelemploye',
            name='employes_nationaux_cdi_femmes',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personnelemploye',
            name='employes_nationaux_cdi_hommes',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personnelemploye',
            name='employes_nationaux_cdi_total',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='responsableorganisation',
            name='fonction',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='responsableorganisation',
            name='nationalite',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='responsableorganisation',
            name='nom_prenom',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
