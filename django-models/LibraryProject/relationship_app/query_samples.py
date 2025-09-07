import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1️⃣ Query all books by a specific author using filter
def books_by_author(author_name):
    authors = Author.objects.filter(name=author_name)
    if authors.exists():
        for author in authors:
            books = Book.objects.filter(author=author)
            print(f"Books by {author.name}: {[book.title for book in books]}")
    else:
        print(f"No author found with name '{author_name}'")

# 2️⃣ List all books in a library using filter
def books_in_library(library_name):
    libraries = Library.objects.filter(name=library_name)
    if libraries.exists():
        for library in libraries:
            books = library.books.all()  # ManyToMany, still use .all()
            print(f"Books in {library.name}: {[book.title for book in books]}")
    else:
        print(f"No library found with name '{library_name}'")

# 3️⃣ Retrieve the librarian for a library using filter
def librarian_for_library(library_name):
    libraries = Library.objects.filter(name=library_name)
    if libraries.exists():
        for library in libraries:
            librarian = Librarian.objects.filter(library=library).first()
            if librarian:
                print(f"Librarian for {library.name}: {librarian.name}")
            else:
                print(f"No librarian assigned to {library.name}")
    else:
        print(f"No library found with name '{library_name}'")

# Example usage
if __name__ == "__main__":
    books_by_author("J.K. Rowling")
    books_in_library("Central Library")
    librarian_for_library("Central Library")
