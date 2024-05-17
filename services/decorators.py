from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.urls import reverse_lazy
from account.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages

# recuperer le modele de l'utilisation
User = get_user_model()

# decorateur de gestion
def gestion_required(view_func):
    """
    Décorateur pour restreindre l'accès aux utilisateurs de type 'gestion'.
    Redirige les utilisateurs 'user' vers une URL spécifiée.
    """
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_user:
            messages.info(request, 'Vous ne pouviez pas acceder a cette page')
            return redirect('index')
        elif not request.user.is_authenticated or not request.user.is_gestion:
            messages.info(request, 'Vous ne pouviez pas acceder a cette page')
            return redirect('index')
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def gestion_user_required(view_func):
    """
    Décorateur pour restreindre l'accès aux utilisateurs de type 'gestion' et 'user'.
    Redirige les autres types d'utilisateurs vers une URL spécifiée.
    """
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_gestion or request.user.is_user:
                # L'utilisateur est autorisé, on exécute la vue
                return view_func(request, *args, **kwargs)
            else:
                # L'utilisateur n'est pas autorisé
                messages.info(request, 'Vous ne pouvez pas accéder à cette page.')
                return redirect('index')
        else:
            # L'utilisateur n'est pas authentifié
            messages.info(request, 'Vous devez être authentifié pour accéder à cette page.')
            return redirect('login')

    return _wrapped_view