from django_seed import Seed
from django.core.management.base import BaseCommand
from .models import Orientation, Formulaire, Secteur, SousSecteur, TitreActivite


class Command(BaseCommand):
    help = "Seeder les informations dans la base de donnee"

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()


        titre_formulaire = [
            { "titre": "FORMULAIRE INFORMATIONS GENERALES" },
            { "titre": "FORMULAIRE PLANIFICATION OPERATIONNELLE" },
            { "titre": "FORMULAIRE SUIVI DES ACTIVITES" }
        ]

        titre_orientation = [
            { "titre": "ORIENTATION STRATEGIQUE 1 : PROMOUVOIR LE POTENTIEL HUMAIN" },
            { "titre": "ORIENTATION STRATEGIQUE 2 : PROMOUVOIR LA COHESION SOCIALE" },
            { "titre": "ORIENTATION STRATEGIQUE 3 : CONSOLIDER LA GOUVERNANCE LOCALE ET INSTITUTIONNELLE" },
            { "titre": "ORIENTATION STRATEGIQUE 4 : PROMOUVOIR UN DEVELOPPEMENT ECONOMIQUE ET ECOLOGIQUE DURABLE" }
        ]
        # Titre Secteur
        titre_secteur = [
            { 'titre': "Secteurs sociaux" },
            { 'titre': "Opérationnalisation de l’intégration systématique de la cohésion sociale dans les interventions de l’OCADES Caritas" },
            { 'titre': "Education des populations des zones d’intervention à la culture de la tolérance et du vivre ensemble" },
            { 'titre': "Secteurs de la gouvernance locale" },
            { 'titre': "Secteurs de la gouvernance institutionnelle" },
            { 'titre': "Secteurs de production" },
            { 'titre': "Secteur de soutien à la production" }
        ]
        # Titre Sous Secteur
        titre_sous_secteur = [
            { "titre": "Alphabétisation" },
            { "titre": "Education" },
            { "titre": "Santé/Nutrition" }
        ]
        # Titre Titre activite
        titre_activite = [
            { "titre": "Réhabilitation de centres d’alpha" },
            { "titre": "Construction de centres d’alpha" }
        ]

        # Enregistrement des donnees
        seeder.add_entity(Formulaire, len(titre_formulaire), titre_formulaire)
        seeder.add_entity(Orientation, len(Orientation), titre_orientation)
        seeder.add_entity(Secteur, len(Secteur), titre_secteur)
        seeder.add_entity(SousSecteur, len(SousSecteur), titre_sous_secteur)
        seeder.add_entity(TitreActivite, len(TitreActivite), titre_activite)

        inserted_pks = seeder.execute()

        self.stdout.write(self.style.SUCCESS('Les donnees ont ete seeders avec succes'))