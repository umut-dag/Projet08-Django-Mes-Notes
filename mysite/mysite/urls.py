from django.urls import path
from notes import views
from django.contrib import admin


""" définition de l’espace de nom de l’application """
app_name = 'notes'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('notesAdd/', views.notesAdd, name='notesAdd'),
    path('notesDelete/<int:notes_id>/', views.notesDelete, name='notesDelete'),
]
