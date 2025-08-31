from bookshelf.models import Book  # replace with your actual app name

# Update the book title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
book.title