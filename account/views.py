from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import re
from django.contrib.auth import get_user_model

from account.forms import SignUpForm


def index(request):
    return render(request, 'service/index.html')


# function creation
def registerPage(request):
    User = get_user_model()
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirmpassword = request.POST.get('password2')
        if all([username, email, password, confirmpassword]):
            try:
                if password != confirmpassword:
                    messages.info(request, "Les mots de passes ne correspondent pas")
                    return redirect('register')
            except:
                pass
            try:
                if User.objects.get(username=username):
                    messages.info(request, "Nom d'utilisateur deja pris")
                    return redirect('register')
            except:
                pass
            try:
                if User.objects.get(email=email):
                    messages.info(request, "L'adresse mail est deja utilisee")
                    return redirect('register')
            except:
                pass
            user = User.objects.create_user(username, email, password)
            user.save()
            messages.success(request, "Votre compte a ete creer! Veuillez-vous connectez")
            return redirect('login')
        else:
            messages.info(request, "Veuillez remplir tout les champs")
            return redirect('register')

    
    return render(request, 'account/register.html')

# function connexion
def loginPage(request):
    User = get_user_model()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = re.match(r"^\S+@\S+\.\S+$", username)
        if email:
            user = User.objects.filter(email=username)
            if user.exists():
                username = user.first().username
        user = authenticate(request, username=username, password=password)  
        # Fonctin d'authentification
        if user is not None:
            login(request, user)
            # retour a la page d'acceuil
            messages.success(request, 'connexion reussie')
            if user.is_user:
                return redirect('/')
            elif user.is_gestion:
                return redirect('/')
        else:
            messages.warning(request, 'Informations incorrectes')
            return render(request, 'account/login.html')

    return render(request, 'account/login.html')


def logoutUser(request):
    logout(request)
    
    messages.info(request, "Deconnecter avec succes")
    return redirect('login')




