# Create Operation - Book Model
from bookshelf.models import Book  # replace with your actual app name

# Create a book instance
book = Book.objects.create(title="1984", author="Ermias", publication_date="1994-09-09")
book

<Book: 1984 by Ermias>
