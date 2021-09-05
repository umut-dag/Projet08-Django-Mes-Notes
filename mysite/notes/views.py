from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Note

def index(request):
    return render(request, 'index.html', {'all_notes': Note.objects.all()})

def notesAdd(request):
    Note(content = request.POST['content_of_inputNote']).save()
    return HttpResponseRedirect("/")
    
def notesDelete(request, notes_id):
    Note.objects.get(id = notes_id).delete()
    return HttpResponseRedirect("/")