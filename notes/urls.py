from django.urls import path
from notes.views import NotesListView, NotesCreateView, success, NotesDetailView, NotesDeleteView, NotesUpdateView

urlpatterns = [
path('', NotesListView.as_view(), name = 'notes'),
path('create/', NotesCreateView.as_view(), name = 'create'),
path('create/success/', success, name = 'success'),
path('note/<int:pk>', NotesDetailView.as_view(), name = 'detail'),
 path('notes/<int:pk>/edit/',
    NotesUpdateView.as_view(), name='notes_edit'),
    path('notes/<int:pk>/delete/',
    NotesDeleteView.as_view(), name='notes_delete'),
]