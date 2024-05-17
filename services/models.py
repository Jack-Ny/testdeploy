from django.db import models
from account.models import User
import numpy as np

# Create your models here.
class Services(models.Model):
    nom = models.CharField(max_length=300, null=True)
    numero = models.FloatField()

    def __str__(self):
        return self.nom
    
# Projects
class Projet(models.Model):
    nom = models.CharField(max_length=100, null=True)
    created = models.DateField(auto_now_add=True, null=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projets', null=True)

    def __str__(self):
        return self.nom

# Titre Activite
class TitreActivite(models.Model):
    titre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.titre
# Secteur
class Secteur(models.Model):
    titre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.titre
# Sous secteur
class SousSecteur(models.Model):
    titre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.titre
# Orientation
class Orientation(models.Model):
    titre = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.titre
# Formulaire
class Formulaire(models.Model):
    titre = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.titre
# Activite
class Activite(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activites', null=True)
    titre = models.CharField(max_length=100, null=True)
    unite_physique = models.CharField(max_length=50, null=True)
    quantite_prevue = models.IntegerField(default=0)
    periode_prevue_debut = models.CharField(max_length=50, null=True)
    periode_prevue_fin = models.CharField(max_length=50, null=True)
    responsable = models.CharField(max_length=50, null=True)
    part_burkina = models.IntegerField(default=0)
    budget_total = models.IntegerField(default=0)
    id_titre_activites = models.ForeignKey(TitreActivite, on_delete=models.CASCADE, related_name="id_titre_activite", null=True)
    id_secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE, related_name="id_secteur", null=True)
    id_sous_secteur = models.ForeignKey(SousSecteur, on_delete=models.CASCADE, related_name="id_sous_secteur", null=True)
    id_orientation = models.ForeignKey(Orientation, on_delete=models.CASCADE, related_name="id_orientation", null=True)
    id_formulaire = models.ForeignKey(Formulaire, on_delete=models.CASCADE, related_name="id_formulaire", null=True)
    id_projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name="id_projet", null=True)

    def __str__(self):
        return self.titre

# Activite
class ActivitePlu(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activiteplus', null=True)
    commune = models.CharField(max_length=50, null=True)
    province = models.CharField(max_length=50, null=True)
    region = models.CharField(max_length=50, null=True)
    paroisse = models.CharField(max_length=50, null=True)
    titre = models.CharField(max_length=100, null=True)
    unite_physique = models.CharField(max_length=50, null=True)
    quantite_prevue = models.IntegerField(default=0)
    periode_prevue_debut = models.CharField(max_length=50, null=True)
    periode_prevue_fin = models.CharField(max_length=50, null=True)
    responsable = models.CharField(max_length=50, null=True)
    cout_realisation = models.IntegerField(default=0)
    contribution_beneficiaire = models.IntegerField(default=0)
    contribution_partenaire = models.IntegerField(default=0)
    part_burkina = models.IntegerField(default=0)
    total_benef_direct = models.IntegerField(default=0)
    nbre_benef_direct_homme = models.IntegerField(default=0)
    nbre_benef_direct_femme = models.IntegerField(default=0)
    id_titre_activites = models.ForeignKey(TitreActivite, on_delete=models.CASCADE, related_name="id_titre_activite_plus", null=True)
    id_secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE, related_name="id_secteur_plus", null=True)
    id_sous_secteur = models.ForeignKey(SousSecteur, on_delete=models.CASCADE, related_name="id_sous_secteur_plus", null=True)
    id_orientation = models.ForeignKey(Orientation, on_delete=models.CASCADE, related_name="id_orientation_plus", null=True)
    id_formulaire = models.ForeignKey(Formulaire, on_delete=models.CASCADE, related_name="id_formulaire_plus", null=True)
    id_projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name="id_projet_plus", null=True)
    
    def __str__(self):
        return self.titre
# Partenaire
class Partenaire(models.Model):
    nom = models.CharField(max_length=50, null=True)
    part = models.IntegerField(default=0)
    id_activite = models.ForeignKey(Activite, on_delete=models.CASCADE, related_name="id_activite", null=True)
    id_activiteplus = models.ForeignKey(ActivitePlu, on_delete=models.CASCADE, related_name='id_activiteplus', null=True)

    def __str__(self):
        return self.nom
    
    def parts_total(self):
        for name, parts in self.nom, self.part:
            result = f"{name} : {parts} /n"
        
        return result


    
class InfosGenerale(models.Model):
    # Informations sur l'organisation
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='generales', null=True)
    id_projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name="infos_generale", null=True)
    nom_org = models.CharField(max_length=50, null=True)
    nature_org = models.CharField(max_length=50, null=True)
    sigle = models.CharField(max_length=50, null=True)
    pays_origine = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=100, null=True)
    province = models.CharField(max_length=100, null=True)
    commune = models.CharField(max_length=100, null=True)
    village = models.CharField(max_length=100, null=True)
    boite_postale = models.CharField(max_length=50, null=True)
    numb_mobile = models.CharField(max_length=50, null=True)
    numb_fixe = models.CharField(max_length=50, null=True)
    adresse_mail = models.CharField(max_length=50, null=True)
    site_web = models.CharField(max_length=50, null=True)
    # Responsable de l'organisation
    nom_complet_resp = models.CharField(max_length=100, null=True)
    nationalite_resp = models.CharField(max_length=50, null=True)
    fonction_resp = models.CharField(max_length=50, null=True)
    numb_fixe_resp = models.CharField(max_length=50, null=True)
    numb_mobile_resp = models.CharField(max_length=50, null=True)
    # Gouvernance interne de l'organisation
    renou_instance = models.CharField(max_length=50, null=True)
    assem_general = models.CharField(max_length=50, null=True)
    session_statut = models.CharField(max_length=50, null=True)
    mandat_bureau = models.CharField(max_length=50, null=True)
    # Repondant pour le canevas
    nom_complet_canevas = models.CharField(max_length=100, null=True)
    numb_fixe_canevas = models.CharField(max_length=50, null=True)
    numb_mobile_canevas = models.CharField(max_length=50, null=True)
    adresse_mail_canevas = models.CharField(max_length=50, null=True)
    # Groupes cibles
    groupes_cibles = models.CharField(max_length=200, null=True)
    autre_groupe = models.CharField(max_length=50, null=True)
    # Employés nationaux CDI
    em_nation_cdi_homme = models.IntegerField(default=0)
    em_nation_cdi_femme = models.IntegerField(default=0)
    # Employes nationaux CDD
    em_nation_cdd_homme = models.IntegerField(default=0)
    em_nation_cdd_femme = models.IntegerField(default=0)
    # Employés expatriés CDI
    em_expa_cdi_homme = models.IntegerField(default=0)
    em_expa_cdi_femme = models.IntegerField(default=0)
    # Employes expatries CDD
    em_expa_cdd_homme = models.IntegerField(default=0)
    em_expa_cdd_femme = models.IntegerField(default=0)
    # Benevol nation CDI
    benevol_nation_homme = models.IntegerField(default=0)
    benevol_nation_femme = models.IntegerField(default=0)
    # Benevol expa CDD
    benevol_expa_homme = models.IntegerField(default=0)
    benevol_expa_femme = models.IntegerField(default=0)
    # Personnel administration
    personnel_admin_homme = models.IntegerField(default=0)
    personnel_admin_femme = models.IntegerField(default=0)
    # ministeres
    numb_convention = models.CharField(max_length=50, null=True)
    date_debut_minis = models.CharField(max_length=50, null=True)
    date_fin_minis = models.CharField(max_length=50, null=True)
    # Collectivite
    numb_proto_collec = models.CharField(max_length=50, null=True)
    date_debut_collec = models.CharField(max_length=50, null=True)
    date_fin_collec = models.CharField(max_length=50, null=True)
    # Convention
    numb_proto_convent = models.CharField(max_length=50, null=True)
    date_debut_convent = models.CharField(max_length=50, null=True)
    date_fin_convent = models.CharField(max_length=50, null=True)
    groupe_cible_total = models.CharField(max_length=300, null=True)
    
    def groupe_total(self):
        liste = self.groupes_cibles
        tableau = np.array(liste)
        result = ", ".join(tableau)
        return result

    def __str__(self):
        return self.nom_org
    
class Partenariat(models.Model):
    nom = models.CharField(max_length=50, null=True)
    numero = models.CharField(max_length=100, null=True)
    date_debut = models.CharField(max_length=50, null=True)
    date_fin = models.CharField(max_length=50, null=True)
    id_general = models.ForeignKey(InfosGenerale, on_delete=models.CASCADE, related_name='id_general_part')

    def __str__(self):
        return self.nom
    
class Objectif(models.Model):
    objectifs = models.CharField(max_length=100, null=True)
    id_general = models.ForeignKey(InfosGenerale, on_delete=models.CASCADE, related_name='id_general', null=True)

    def __str__(self):
        return self.objectifs

    def objectifsListe(self):
        for obj in self.objectifs:
            list = f'{obj}/n'

        return list
        





