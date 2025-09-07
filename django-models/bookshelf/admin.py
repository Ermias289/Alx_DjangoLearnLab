from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Custom method to display only the year
    def publication_year(self, obj):
        return obj.publication_date.year

    publication_year.admin_order_field = 'publication_date'  # enables sorting by date
    publication_year.short_description = 'Publication Year'  # column header in admin

    # Admin list configuration
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('author', 'publication_date')  # filter by full date
    ordering = ('publication_date',)
