from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language, Catalog, CatalogCase


admin.site.register(Genre)
admin.site.register(Language)


class BooksInline(admin.TabularInline):
    model = Book

class CatalogsInline(admin.TabularInline):
    model = Catalog


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name',
                    'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

class CatalogsCaseInline(admin.TabularInline):
    model = CatalogCase


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


admin.site.register(Book, BookAdmin)


class CatalogAdmin(admin.ModelAdmin):
    list_display = ('title', 'name')
    inlines = [CatalogsCaseInline]


admin.site.register(Catalog, CatalogAdmin)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )


@admin.register(CatalogCase)
class CatalogCaseAdmin(admin.ModelAdmin):
    list_display = ('catalog', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('catalog', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

