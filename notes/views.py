from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView, DetailView
from notes.models import Note
from django.views.generic.edit import UpdateView,DeleteView

class NotesUpdateView(UpdateView):
    model = Note   
    template_name = 'notes_edit.html'
    fields = ['title', 'content']
    success_url = reverse_lazy ('notes')

class NotesDeleteView(DeleteView):
    model = Note
    template_name = 'notes_delete.html'
    success_url = reverse_lazy ('notes')

class NotesDetailView(DetailView):
    model = Note
    template_name = 'notes_detail.html'
    context_object_name = 'note'

class NotesListView(ListView):
    model = Note
    template_name = 'notes.html'
    context_object_name = 'note'

class NotesCreateView(CreateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'create.html'
    success_url = 'success'
    
def success(request):
   return render(request, 'success.html')

