from django_seeding import seeders
from django_seeding.seeder_registry import SeederRegistry
from .models import TitreActivite, Secteur, SousSecteur, Orientation, Formulaire

@SeederRegistry.register
class M1Seeder(seeders.JSONFileModelSeeder):
    id = "M1Seeder"
    priority = 1
    model = Formulaire
    json_file_path = 'json_files/M1Seeder.json'

@SeederRegistry.register
class M2Seeder(seeders.JSONFileModelSeeder):
    id = "M2Seeder"
    priority = 2
    model = Orientation
    json_file_path = 'json_files/M2Seeder.json'

@SeederRegistry.register
class M3Seeder(seeders.JSONFileModelSeeder):
    id = "M3Seeder"
    priority = 3
    model = Secteur
    json_file_path = 'json_files/M3Seeder.json'

@SeederRegistry.register
class M4Seeder(seeders.JSONFileModelSeeder):
    id = "M4Seeder"
    priority = 4
    model = SousSecteur
    json_file_path = 'json_files/M4Seeder.json'


@SeederRegistry.register
class M5Seeder(seeders.JSONFileModelSeeder):
    id = "M5Seeder"
    priority = 5
    model = TitreActivite
    json_file_path = 'json_files/M5Seeder.json'