from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm

# Create your views here.
def notes_list(request):
    category_filter = request.GET.get('category')
    if category_filter:
        notes = Note.objects.filter(category=category_filter)
    else:
        notes = Note.objects.all()
    return render(request, 'notes_app/notes.html', {'notes': notes})

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes_list')
    else:
        form = NoteForm()
    return render(request, 'notes_app/notes_form.html', {'form': form})

def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes_app/notes_form.html', {'form': form})

def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('notes_list')
    return render(request, 'notes_app/confirm_delete.html', {'note': note})
    
    
        
