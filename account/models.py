from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField('Est un administrateur', default=False)
    is_user = models.BooleanField('Est un utilisateur', default=False)
    is_gestion = models.BooleanField('Est un gestionnaire', default=False)
