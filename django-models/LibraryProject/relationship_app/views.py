from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library
from .models import Book
from django.http import HttpResponse
from .models import Book
from django.views.generic.detail import DetailView

def list_books(request):
    books = Book.objects.all()
    # render the template and pass books as context
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # <- include app name for clarity
    context_object_name = 'library'