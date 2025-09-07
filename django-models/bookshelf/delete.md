from bookshelf.models import Book  # replace with your actual app name

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Check all books
Book.objects.all()