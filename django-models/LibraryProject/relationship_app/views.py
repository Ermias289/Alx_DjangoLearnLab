from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library
from .models import Book
from django.http import HttpResponse
from .models import Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login

def list_books(request):
    books = Book.objects.all()
    # render the template and pass books as context
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # <- include app name for clarity
    context_object_name = 'library'


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# --- Registration ---
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# --- Login ---
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')  # redirect anywhere (example: books list)
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


# --- Logout ---
@login_required
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile

# --- Role check helpers ---
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# --- Admin View ---
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


# --- Librarian View ---
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


# --- Member View ---
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
