from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),
]


from django.urls import path
from .views import list_books, LibraryDetailView, register_view, login_view, logout_view

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # authentication routes
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]


views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="
                                                                         

                                                                         from django.urls import path
from .views import list_books, LibraryDetailView, register_view, login_view, logout_view
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    # previous views
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # role-based views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]
