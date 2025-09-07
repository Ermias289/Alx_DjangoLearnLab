from your_app_name.models import Book  # replace your_app_name with your actual app name

# Create a book instance
book = Book.objects.create(title="1984", author="Ermias", publication_date="1994-09-09")
book


<Book: 1984 by Ermias>




# Retrieve the created book
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_date


('1984', 'Ermias', datetime.date(1994, 9, 9))


# Update the title of the book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
book.title

'Nineteen Eighty-Four'


# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Check all books
Book.objects.all()


<QuerySet []>
