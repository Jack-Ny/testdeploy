from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profil/', views.profils, name='profils'),
    path('change_password/', views.change_password, name='change_password'),
    path('service/', views.service, name='service'),
    path('generate_pdf_generale/', views.generate_pdf_generale, name='generate_pdf_generale'),
    path('generate_excel_generale', views.generate_excel_generale, name='generate_excel_generale'),
    path('generate_word_generale', views.generate_word_generale, name='generate_word_generale'),
    path('generate_pdf_planification/', views.generate_pdf_planification, name='generate_pdf_planification'),
    path('generate_word_planification/', views.generate_word_planification, name='generate_word_planification'),
    path('generate_excel_planification/', views.generate_excel_planification, name='generate_excel_planification'),
    path('generate_pdf_suivi/', views.generate_pdf_suivi, name='generate_pdf_suivi'),
    path('generate_word_suivi/', views.generate_word_suivi, name='generate_word_suivi'),
    path('generate_excel_suivi/', views.generate_excel_suivi, name='generate_excel_suivi'),
    path('synthese_generale/', views.globale_generale, name='globale_generale'),
    path('synthese_planification/', views.globale_planification, name='globale_planification'),
    path('synthese_suivi/', views.globale_suivi, name='globale_suivi'),
    path('create_projet/', views.create_projet, name='create_projet'),
    path('success/', views.success, name='success'),
    path('choisir_modifier/', views.choisir_modifier, name='choisir_modifier'),

    path('projet/', views.projet, name='projet'),
    path('projet/<int:projet_id>/', views.choix_projet, name='choix_projet'),
    
    path('projet/<int:projet_id>/choix_form/generales/', views.generales, name='generales'),
    path('projet/<int:projet_id>/choix_form/generales/ajouter_general/', views.ajouter_general, name='ajouter_general'),
    path('projet/<int:projet_id>/choix_form/generales/modifier_general/<int:gen_id>/', views.modifier_general, name='modifier_general'),
    path('projet/<int:projet_id>/choix_form/generales/voir_general/<int:gen_id>/', views.view_generale, name='view_generale'),

    path('projet/<int:projet_id>/choix_form/planification/', views.activites, name='activites'),
    path('projet/<int:projet_id>/choix_form/planification/ajouter_activiter/', views.ajouter_planification, name='ajouter_planification'),
    path('projet/<int:projet_id>/choix_form/planification/modifier_activiter/<int:activite_id>/', views.modifier_planification, name='modifier_planification'),
    path('projet/<int:projet_id>/choix_form/planification/voir_activiter/<int:activite_id>/', views.view_activite, name='view_activite'),

    path('projet/<int:projet_id>/choix_form/suivi/', views.activitesplus, name='activitesplus'),
    path('projet/<int:projet_id>/choix_form/suivi/ajouter_activiter/', views.ajouter_suivi, name='ajouter_suivi'),
    path('projet/<int:projet_id>/choix_form/suivi/modifier_activiter/<int:activite_id>/', views.modifier_suivi, name='modifier_suivi'),
    path('projet/<int:projet_id>/choix_form/suivi/voir_activiter/<int:activite_id>/', views.view_activiteplus, name='view_activiteplus')
    
]
