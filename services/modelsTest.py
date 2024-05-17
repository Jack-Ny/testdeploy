from django.db import models


ORIENTATION_CHOICES = [
    ('os1', 'PROMOUVOIR LE POTENTIEL HUMAIN'),
    ('os2', 'PROMOUVOIR LA COHESION SOCIALE'),
    ('os3', 'CONSOLIDER LA GOUVERNANCE LOCALE ET INSTITUTIONNELLE'),
    ('os4', 'PROMOUVOIR UN DEVELOPPEMENT ECONOMIQUE ET ECOLOGIQUE DURABLE'),
]

SECTEUR_CHOICES = [
    ('secteur 1', 'Secteurs sociaux'),
    ('secteur 2', 'Secteurs de la gouvernance locale'),
    ('secteur 3', 'Secteurs de la gouvernance institutionnelle'),
    ('secteur 4', 'Secteurs de production'),
    ('secteur 5', 'Secteur de soutien à la production'),
]

SOUS_SECTEURS_CHOICES = [
    ('sous 1', 'Agriculture'),
    ('sous 2', 'Elevage'),
    ('sous 3', 'Environnement'),
    ('sous 4', 'Volet Hydraulique de production'),
    ('sous 5', 'Services en énergie mécanique, en énergie électrique, et en énergie renouvelable'),
    ('sous 6', 'Services de crédit, subvention pour AGR, equipements et infrastructures'),
]

# Create your models here.
class Services(models.Model):
    nom = models.CharField(max_length=300, null=True)
    numero = models.FloatField()

    def __str__(self):
        return self.nom

class Project(models.Model):
    name = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

# Formulaire Information generales
class InformationGenerale(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="information_general", null=True)
    titre = models.CharField(max_length=100, null=True)
    CHOIX_ORGANISATION = [
        ('ONG', 'ONG'),
        ('Association', 'Association'),
        ('Fondation', 'Fondation'),
    ]
    nature_organisation = models.CharField(max_length=50, choices=CHOIX_ORGANISATION, null=True)
    sigle = models.CharField(max_length=50, null=True)
    pays_origine = models.CharField(max_length=50, null=True)
    region = models.CharField(max_length=50, null=True)
    province = models.CharField(max_length=50, null=True)
    commune = models.CharField(max_length=50, null=True)
    village = models.CharField(max_length=50, null=True)
    boite_postale = models.CharField(max_length=50, null=True)
    telephone_fixe = models.CharField(max_length=50, null=True)
    telephone_mobile = models.CharField(max_length=50, null=True)
    email_professionnel  = models.CharField(max_length=50, null=True)
    site_web = models.CharField(max_length=50, null=True)
    objectifs_organisation = models.CharField(max_length=500, null=True)
    CHOIX_GROUPE_CIBLE = [
        ('Femmes', 'Femmes'),
        ('Enfants/Nourissons', 'Enfants/Nourissons'),
        ('Eleves/Etudiants/Apprenants', 'Eleves/Etudiants/Apprenants'),
        ('OEV', 'OEV'),
        ('Personne en situation de handicap', 'Personne en situation de handicap'),
        ('Refugies', 'Refugies'),
        ('Veuves/Veufs', 'Veuves/Veufs'),
        ('PV/VIH', 'PV/VIH'),
        ('Producteurs', 'Producteurs'),
        ('Organisations paysannes', 'Organisations paysannes'),
        ('OSC', 'OSC'),
        ('Acteurs communaux', 'Acteurs communaux'),
        ('PDI', 'PDI'),
        ('autre', 'Autre(a preciser)')
    ]
    groupe_cible = models.CharField(max_length=50, choices=CHOIX_GROUPE_CIBLE, null=True)
    choix_personnaliser = models.CharField(max_length=50, null=True)

# Responsable de l'organisation
class ResponsableOrganisation(models.Model):
    information_general = models.OneToOneField(InformationGenerale, on_delete=models.CASCADE, related_name="responsable_organisation")
    nom_prenom = models.CharField(max_length=150, null=True)
    nationalite = models.CharField(max_length=50, null=True)
    fonction = models.CharField(max_length=50, null=True)
# Gouvernance interne de l'organisation / Tenue des rencontres statutaires des instances de l'organisation
class GouvernanceInterne(models.Model):
    information_general = models.OneToOneField(InformationGenerale, on_delete=models.CASCADE, related_name="gouvernance_interne")
    DESIGNATION_CHOICES = [
        ('renouvellement_instances', 'Dernier renouvellement des Instances dirigeantes'),
        ('assemblee_generale', 'Dernière Assemblée Générale Ordinaire'),
        ('session_bureau_executif', 'Dernière session statutaire du bureau exécutif'),
        ('mandat_bureau_executif', 'Durée du mandat du bureau exécutif'),
    ]
    designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICES, null=True)
    date_annee = models.DateField()
# Répondant pour le canevas de collecte
class RepondantCanvas(models.Model):
    information_general = models.OneToOneField(InformationGenerale, on_delete=models.CASCADE, related_name="repondant_canvas")
    nom_complet = models.CharField(max_length=100)
    contact_fixe = models.CharField(max_length=50)
    contact_mobile = models.CharField(max_length=50)
    adresse_mail = models.EmailField(max_length=40)
# Personnel employe
class PersonnelEmploye(models.Model):
    information_general = models.OneToOneField(InformationGenerale, on_delete=models.CASCADE, related_name="personnel_employe")
    # Employés nationaux Contrat à Durée Indéterminée (CDI)
    employes_nationaux_cdi_hommes = models.CharField(max_length=50, null=True)
    employes_nationaux_cdi_femmes = models.CharField(max_length=50, null=True)
    employes_nationaux_cdi_total = models.CharField(max_length=50, null=True)
    # Employés nationaux Contrat à Durée déterminée (CDD)
    employes_nationaux_cdd_hommes = models.CharField(max_length=50, null=True)
    employes_nationaux_cdd_femmes = models.CharField(max_length=50, null=True)
    employes_nationaux_cdd_total = models.CharField(max_length=50, null=True)
    # Employés expatriés Contrat à Durée Indéterminée (CDI)
    employes_expatries_cdi_hommes = models.CharField(max_length=50, null=True)
    employes_expatries_cdi_femmes = models.CharField(max_length=50, null=True)
    employes_expatries_cdi_total = models.CharField(max_length=50, null=True)
    # Employés expatriés Contrat à Durée déterminée (CDD)
    employes_expatries_cdd_hommes = models.CharField(max_length=50, null=True)
    employes_expatries_cdd_femmes = models.CharField(max_length=50, null=True)
    employes_expatries_cdd_total = models.CharField(max_length=50, null=True)
# Benevoles ou volontaires
class Benevole(models.Model):
    information_general = models.OneToOneField(InformationGenerale, on_delete=models.CASCADE, related_name="benevole")
    # Bénévoles ou volontaires Nationaux
    benevoles_nationaux_hommes = models.CharField(max_length=50, null=True)
    benevoles_nationaux_femmes = models.CharField(max_length=50, null=True)
    benevoles_nationaux_total = models.CharField(max_length=50, null=True)
    # Bénévoles ou volontaires Expatriés
    benevoles_expatries_hommes = models.CharField(max_length=50, null=True)
    benevoles_expatries_femmes = models.CharField(max_length=50, null=True)
    benevoles_expatries_total = models.CharField(max_length=50, null=True)

# Personnel de l'Administration publique en détachement
class PersonnelAdministration(models.Model):
    information_general = models.OneToOneField(InformationGenerale, on_delete=models.CASCADE, related_name="personnel_administration")
    personnel_admin_homme = models.CharField(max_length=50, null=True)
    personnel_admin_femme = models.CharField(max_length=50, null=True)
    personnel_admin_total = models.CharField(max_length=50, null=True)

# Partenariats / collaborations
class Partenaire(models.Model):
    information_general = models.OneToOneField(InformationGenerale, on_delete=models.CASCADE, related_name="partenaire")
    MINISTERE_CHOICES = [
        ('ministere1', 'Ministère 1'),
        ('ministere2', 'Ministère 2'),
        ('ministere3', 'Ministère 3'),
    ]
    # Partenariats avec les Ministères
    ministere = models.CharField(max_length=100, choices=MINISTERE_CHOICES, null=True)
    date_debut_effet_ministere = models.DateField()
    date_fin_effet_ministere = models.DateField()
    # Partenariats avec les Collectivités territoriales
    protocole_entente_collectivite = models.CharField(max_length=100, null=True)
    date_debut_effet_collectivite = models.DateField()
    date_fin_effet_collectivite = models.DateField()
    # Conventions spécifiques
    protocole_entente_convention = models.CharField(max_length=100, null=True)
    date_debut_effet_convention = models.DateField()
    date_fin_effet_convention = models.DateField()





# Formulaire Planification Operationnelle
class PlanificationOperationnelle(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="planification_operationnelle", null=True)
    titre = models.CharField(max_length=200, null=True)

class SuiviActivites(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="suivi_activite", null=True)
    titre = models.CharField(max_length=50, null=True)

# Orientation Strategique 1 :
class Orientation1(models.Model):
    planification = models.ForeignKey(PlanificationOperationnelle, on_delete=models.CASCADE, related_name="orientation1", null=True)
    titre = models.CharField(max_length=200, null=True)

# ----------------- Secteur sociaux ---------------------
# Alphabetisation
# Activites 1
class Activites1_1(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_1", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0


# Activites 2
class Activites1_2(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_2", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Activites 3
class Activites1_3(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_3", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Activites 4
class Activites1_4(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_4", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Activites 5
class Activites1_5(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_5", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

    

# Activites 6
class Activites1_6(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_6", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Activites 7
class Activites1_7(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_7", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Education
# Activites 8
class Activites1_8(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_8", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Sante/Nutrition
# Activites 9
class Activites1_9(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_9", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Activites 10
class Activites1_10(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_10", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0


# Activites 11
class Activites1_11(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_11", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0


# Activites 12
class Activites1_12(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_12", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0


# Activites 13
class Activites1_13(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_13", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0


# Activites 14
class Activites1_14(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_14", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0


# Activites 15
class Activites1_15(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_15", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0


# Activites 16
class Activites1_16(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_16", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0


# Activites 17
class Activites1_17(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_17", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0


# Activites 18
class Activites1_18(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_18", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0


# Activites 19
class Activites1_19(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_19", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0


# Activites 20
class Activites1_20(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_20", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0


# Activites 21
class Activites1_21(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_21", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0


# Activites 22
class Activites1_22(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_22", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0


# Activites 23
class Activites1_23(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_23", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0


# Activites 24
class Activites1_24(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_24", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Assainissement
# Activites 25
class Activites1_25(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_25", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Activites 26
class Activites1_26(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_26", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Activites 27
class Activites1_27(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_27", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Activites 28
class Activites1_28(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_28", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Activites 29
class Activites1_29(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_29", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Activites 30
class Activites1_30(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_30", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Activites 31
class Activites1_31(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_31", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Activites 32
class Activites1_32(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_32", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Activites 33
class Activites1_33(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_33", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Activites 34
class Activites1_34(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_34", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Activites 35
class Activites1_35(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_35", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Hydraulique/eau potable
# Activites 36
class Activites1_36(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_36", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Activites 37
class Activites1_37(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_37", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Activites 38
class Activites1_38(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_38", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Activites 39
class Activites1_39(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_39", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
    somme_part_etat_financier = models.IntegerField(default=0)

    def budget_total(self):
        if self.part_etat_financier:
            parts = self.part_etat_financier.replace("[", "").replace("]", "").replace("'", "").split(',')

            parts_int = []
            for part in parts:
                if part.strip().isdigit():
                    parts_int.append(int(part.strip()))
            
            somme = sum(parts_int)
            return somme
        else:
            return 0

# Activites 40
class Activites1_40(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_40", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 41
class Activites1_41(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_41", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 42
class Activites1_42(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_42", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 43
class Activites1_43(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_43", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Art culture et sport
# Activites 44
class Activites1_44(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_44", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 45
class Activites1_45(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_45", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 46
class Activites1_46(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_46", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 47
class Activites1_47(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_47", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 48
class Activites1_48(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_48", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 49
class Activites1_49(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_49", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)


# Rehabilitation a base communautaire (RBC) / Consultation et soins
# Activites 50
class Activites1_50(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_50", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 51
class Activites1_51(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_51", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 52
class Activites1_52(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_52", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 53
class Activites1_53(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_53", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 54
class Activites1_54(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_54", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 55
class Activites1_55(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_55", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Rehabilitation a base communautaire (RBC) / Education prescolaire et primaires des personnes handicapes
# Activites 56
class Activites1_56(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_56", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 57
class Activites1_57(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_57", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Rehabilitaion a base communautaire (RBC) / Moyens de subsistance pour personnes handicapes
# Activites 58
class Activites1_58(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_58", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 59
class Activites1_59(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_59", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 60
class Activites1_60(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_60", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Rehabilitation a base communautaire (RBC) / Actions de formations, de sensibilisation et de plaidoyer
# Activites 61
class Activites1_61(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_61", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 62
class Activites1_62(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_62", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 63
class Activites1_63(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_63", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 64
class Activites1_64(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_64", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 65
class Activites1_65(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_65", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 66
class Activites1_66(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_66", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Actions/Social urgence au profit des sinistres et des personnes vulnerable
# Activites 67
class Activites1_67(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_67", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 68
class Activites1_68(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_68", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 69
class Activites1_69(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_69", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 70
class Activites1_70(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_70", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 71
class Activites1_71(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_71", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 72
class Activites1_72(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_72", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 73
class Activites1_73(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_73", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 74
class Activites1_74(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_74", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 75
class Activites1_75(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_75", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 76
class Activites1_76(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_76", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 77
class Activites1_77(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_77", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 78
class Activites1_78(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_78", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 79
class Activites1_79(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_79", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 80
class Activites1_80(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_80", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 81
class Activites1_81(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_81", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 82
class Activites1_82(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_82", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 83
class Activites1_83(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_83", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 84
class Activites1_84(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_84", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 85
class Activites1_85(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_85", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 86
class Activites1_86(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_86", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 87
class Activites1_87(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_87", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 88
class Activites1_88(models.Model):
    orientation = models.ForeignKey(Orientation1, on_delete=models.CASCADE, related_name="activite1_88", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

#---------------------------------------------------------------------------------------------------------------------------------------
# Orientation Strategique 2 :
class Orientation2(models.Model):
    planification = models.ForeignKey(PlanificationOperationnelle, on_delete=models.CASCADE, related_name="orientation2", null=True)
    titre = models.CharField(max_length=200, null=True)

# ---------------------------- Education de population de zones d'intervention .......
# Activites 1
class Activites2_1(models.Model):
    orientation = models.ForeignKey(Orientation2, on_delete=models.CASCADE, related_name="activite2_1", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 2
class Activites2_2(models.Model):
    orientation = models.ForeignKey(Orientation2, on_delete=models.CASCADE, related_name="activite2_2", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 3
class Activites2_3(models.Model):
    orientation = models.ForeignKey(Orientation2, on_delete=models.CASCADE, related_name="activite2_3", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)


# ----------------------------------------------------------------------------------------------------------------------------------
# Orientation Strategique 3 :
class Orientation3(models.Model):
    planification = models.ForeignKey(PlanificationOperationnelle, on_delete=models.CASCADE, related_name="orientation3", null=True)
    titre = models.CharField(max_length=200, null=True)

# -----------------Secteur de la gouvernance locale---------------------
# Activites 1
class Activites3_1(models.Model):
    project = models.ForeignKey(Orientation3, on_delete=models.CASCADE, related_name="activites3_1", null=True)
    orientation = models.ForeignKey(Orientation3, on_delete=models.CASCADE, related_name="activite3_1", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50, null=True)
    quantite_prevue = models.CharField(max_length=50, null=True)
    periode_prevue = models.CharField(max_length=100, null=True)
    responsable_projet = models.CharField(max_length=50, null=True)
    part_etat_burkinabe = models.CharField(max_length=50, null=True)
    part_etat_financier = models.CharField(max_length=500, null=True)


# Activites 2
class Activites3_2(models.Model):
    orientation = models.ForeignKey(Orientation3, on_delete=models.CASCADE, related_name="activite3_2", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.DateField()
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 3
class Activites3_3(models.Model):
    orientation = models.ForeignKey(Orientation3, on_delete=models.CASCADE, related_name="activite3_3", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.DateField()
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 4
class Activites3_4(models.Model):
    orientation = models.ForeignKey(Orientation3, on_delete=models.CASCADE, related_name="activite3_4", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.DateField()
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 5
class Activites3_5(models.Model):
    orientation = models.ForeignKey(Orientation3, on_delete=models.CASCADE, related_name="activite3_5", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.DateField()
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 6
class Activites3_6(models.Model):
    orientation = models.ForeignKey(Orientation3, on_delete=models.CASCADE, related_name="activite3_6", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.DateField()
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 7
class Activites3_7(models.Model):
    orientation = models.ForeignKey(Orientation3, on_delete=models.CASCADE, related_name="activite3_7", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.DateField()
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 8
class Activites3_8(models.Model):
    orientation = models.ForeignKey(Orientation3, on_delete=models.CASCADE, related_name="activite3_8", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.DateField()
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 9
class Activites3_9(models.Model):
    orientation = models.ForeignKey(Orientation3, on_delete=models.CASCADE, related_name="activite3_9", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.DateField()
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 10
class Activites3_10(models.Model):
    orientation = models.ForeignKey(Orientation3, on_delete=models.CASCADE, related_name="activite3_10", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.DateField()
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 11
class Activites3_11(models.Model):
    orientation = models.ForeignKey(Orientation3, on_delete=models.CASCADE, related_name="activite3_11", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.DateField()
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 12
class Activites3_12(models.Model):
    orientation = models.ForeignKey(Orientation3, on_delete=models.CASCADE, related_name="activite3_12", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.DateField()
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 13
class Activites3_13(models.Model):
    orientation = models.ForeignKey(Orientation3, on_delete=models.CASCADE, related_name="activite3_13", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.DateField()
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 14
class Activites3_14(models.Model):
    orientation = models.ForeignKey(Orientation3, on_delete=models.CASCADE, related_name="activite3_14", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.DateField()
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 15
class Activites3_15(models.Model):
    orientation = models.ForeignKey(Orientation3, on_delete=models.CASCADE, related_name="activite3_15", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.DateField()
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 16
class Activites3_16(models.Model):
    orientation = models.ForeignKey(Orientation3, on_delete=models.CASCADE, related_name="activite3_16", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.DateField()
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 17
class Activites3_17(models.Model):
    orientation = models.ForeignKey(Orientation3, on_delete=models.CASCADE, related_name="activite3_17", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.DateField()
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 18
class Activites3_18(models.Model):
    orientation = models.ForeignKey(Orientation3, on_delete=models.CASCADE, related_name="activite3_18", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.DateField()
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)


# ----------------- Secteur de la gouvernance institutionnelle ---------------------
# Activites 29
class Activites3_19(models.Model):
    orientation = models.ForeignKey(Orientation3, on_delete=models.CASCADE, related_name="activite3_19", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.DateField()
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

    
# -----------------------------------------------------------------------------------------------------------------------------------
# Orientation Strategique 4 :
class Orientation4(models.Model):
    planification = models.ForeignKey(PlanificationOperationnelle, on_delete=models.CASCADE, related_name="orientation4", null=True)
    titre = models.CharField(max_length=200, null=True)

# ----------------- Secteur de production ---------------------
# Agriculture
# Activites 1
class Activites4_1(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_1", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 2
class Activites4_2(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_2", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 3
class Activites4_3(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_3", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 4
class Activites4_4(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_4", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 5
class Activites4_5(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_5", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 6
class Activites4_6(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_6", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 7
class Activites4_7(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_7", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 8
class Activites4_8(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_8", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 9
class Activites4_9(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_9", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 10
class Activites4_10(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_10", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 11
class Activites4_11(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_11", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 12
class Activites4_12(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_12", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 13
class Activites4_13(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_13", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 14
class Activites4_14(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_14", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 15
class Activites4_15(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_15", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 16
class Activites4_16(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_16", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 17
class Activites4_17(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_17", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 18
class Activites4_18(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_18", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 19
class Activites4_19(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_19", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 20
class Activites4_20(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_20", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 21
class Activites4_21(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_21", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 22
class Activites4_22(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_22", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 23
class Activites4_23(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_23", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 24
class Activites4_24(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_24", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 25
class Activites4_25(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_25", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 26
class Activites4_26(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_26", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 27
class Activites4_27(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_27", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 28
class Activites4_28(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_28", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Elevage (22)
# Activites 29
class Activites4_29(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_29", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 30
class Activites4_30(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_30", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 31
class Activites4_31(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_31", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 32
class Activites4_32(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_32", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 33
class Activites4_33(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_33", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 34
class Activites4_34(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_34", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 35
class Activites4_35(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_35", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 36
class Activites4_36(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_36", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 37
class Activites4_37(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_37", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 38
class Activites4_38(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_38", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 39
class Activites4_39(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_39", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 40
class Activites4_40(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_40", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 41
class Activites4_41(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_41", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 42
class Activites4_42(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_42", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 43
class Activites4_43(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_43", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 44
class Activites4_44(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_44", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 45
class Activites4_45(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_45", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 46
class Activites4_46(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_46", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 47
class Activites4_47(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_47", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 48
class Activites4_48(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_48", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 49
class Activites4_49(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_49", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 50
class Activites4_50(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_50", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Environnement (20)
# Activites 51
class Activites4_51(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_51", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 52
class Activites4_52(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_52", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 53
class Activites4_53(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_53", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 54
class Activites4_54(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_54", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 55
class Activites4_55(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_55", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 56
class Activites4_56(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_56", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 57
class Activites4_57(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_57", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 58
class Activites4_58(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_58", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 59
class Activites4_59(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_59", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 60
class Activites4_60(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_60", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 61
class Activites4_61(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_61", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 62
class Activites4_62(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_62", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 63
class Activites4_63(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_63", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 64
class Activites4_64(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_64", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 65
class Activites4_65(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_65", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 66
class Activites4_66(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_66", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 67
class Activites4_67(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_67", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 68
class Activites4_68(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_68", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 69
class Activites4_69(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_69", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 70
class Activites4_70(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_70", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# ------------------- Secteur de soutien -----------------------
# Volet hydraulique de production ........(14)
# Activites 71
class Activites4_71(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_71", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 72
class Activites4_72(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_72", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 73
class Activites4_73(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_73", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 74
class Activites4_74(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_74", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 75
class Activites4_75(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_75", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 76
class Activites4_76(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_76", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 77
class Activites4_77(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_77", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 78
class Activites4_78(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_78", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 79
class Activites4_79(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_79", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 80
class Activites4_80(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_80", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 81
class Activites4_81(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_81", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 82
class Activites4_82(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_82", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 83
class Activites4_83(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_83", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 84
class Activites4_84(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_84", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Service en energie ..... (9)
# Activites 85
class Activites4_85(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_85", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 86
class Activites4_86(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_86", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 87
class Activites4_87(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_87", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 88
class Activites4_88(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_88", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 89
class Activites4_89(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_89", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 90
class Activites4_90(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_90", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 91
class Activites4_91(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_91", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 92
class Activites4_92(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_92", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 93
class Activites4_93(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_93", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)


# Service de credit, subvention pour AGR, equipements et infrastructure
# Activites 94
class Activites4_94(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_94", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 95
class Activites4_95(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_95", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 96
class Activites4_96(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_96", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 97
class Activites4_97(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_97", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 98
class Activites4_98(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_98", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 99
class Activites4_99(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_99", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 100
class Activites4_100(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_100", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 101
class Activites4_101(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_101", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 102
class Activites4_102(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_102", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 103
class Activites4_103(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_103", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 104
class Activites4_104(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_104", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 105
class Activites4_105(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_105", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 106
class Activites4_106(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_106", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 107
class Activites4_107(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_107", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 108
class Activites4_108(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_108", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 109
class Activites4_109(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_109", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 110
class Activites4_110(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_110", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 111
class Activites4_111(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_111", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 112
class Activites4_112(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_112", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 113
class Activites4_113(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_113", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)

# Activites 114
class Activites4_114(models.Model):
    orientation = models.ForeignKey(Orientation4, on_delete=models.CASCADE, related_name="activite4_114", null=True)
    secteur = models.CharField(max_length=100, choices=SECTEUR_CHOICES)
    sous_secteur = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=100)
    unite_physique = models.CharField(max_length=50)
    quantite_prevue = models.CharField(max_length=50)
    periode_prevue = models.CharField(max_length=100)
    responsable_projet = models.CharField(max_length=50)
    part_etat_burkinabe = models.CharField(max_length=50)
    part_etat_financier = models.CharField(max_length=500, null=True)
