# Retrieve Operation - Book Model

from bookshelf.models import Book  # replace with your actual app name

# Retrieve the created book
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_date

('1984', 'Ermias', datetime.date(1994, 9, 9))

