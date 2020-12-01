from django.shortcuts import render

from library_app.models import Book, Author, BookInstance, Genre, Catalog, CatalogCase

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()    
    num_authors = Author.objects.count()
    num_catalogs = Catalog.objects.all().count()
    num_cases = CatalogCase.objects.all().count()
    num_cases_available = CatalogCase.objects.filter(status__exact='a').count() 

    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_catalogs': num_catalogs,
        'num_cases': num_cases,
        'num_cases_available': num_cases_available,
    }

    
    return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 4


class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4

class AuthorDetailView(generic.DetailView):
    model = Author

class CatalogListView(generic.ListView):
    model = Catalog
    paginate_by = 4

class CatalogDetailView(generic.DetailView):
    model = Catalog


from django.contrib.auth.mixins import LoginRequiredMixin


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'library_app/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class LoanedCatalogsByUserListView(LoginRequiredMixin, generic.ListView):
    model = CatalogCase
    template_name = 'library_app/catalogcase_list_borrowed_user.html'

def get_queryset(self):
        return CatalogCase.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')



from django.contrib.auth.mixins import PermissionRequiredMixin


class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
    model = BookInstance
    permission_required = 'library.can_mark_returned'
    template_name = 'library_app/bookinstance_list_borrowed_all.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')   


class LoanedCatalogsAllListView(PermissionRequiredMixin, generic.ListView):
    model = CatalogCase
    permission_required = 'library.can_mark_returned'
    template_name = 'library_app/catalogcase_list_borrowed_all.html'
    paginate_by = 10

def get_queryset(self):
        return CatalogCase.objects.filter(status__exact='o').order_by('due_back')

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import permission_required

from library_app.forms import RenewBookForm
from library_app.forms import RenewCatalogForm

@permission_required('library.can_mark_returned')
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)
    if request.method == 'POST':
        form = RenewBookForm(request.POST)
        if form.is_valid():
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            return HttpResponseRedirect(reverse('all-borrowed-books'))
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(days=30)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'library_app/book_renew_librarian.html', context)

@permission_required('library.can_mark_returned')
def renew_catalog_librarian(request, pk):
    catalog_case = get_object_or_404(CatalogCase, pk=pk)
    if request.method == 'POST':
        form = RenewCatalogForm(request.POST)
        if form.is_valid():
            catalog_case.due_back = form.cleaned_data['renewal_date']
            catalog_case.save()

            return HttpResponseRedirect(reverse('all-borrowed-catalogs'))
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(days=30)
        form = RenewCatalogForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'catalog_case': catalog_case,
    }

    return render(request, 'library_app/catalog_renew_librarian.html', context)


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author


class AuthorCreate(PermissionRequiredMixin, CreateView):
    model = Author
    fields = '__all__'
    initial = {'date_of_death': '05/01/2018'}
    permission_required = 'library.can_mark_returned'


class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    permission_required = 'library.can_mark_returned'


class AuthorDelete(PermissionRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
    permission_required = 'library.can_mark_returned'


class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    permission_required = 'library.can_mark_returned'


class BookUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = '__all__'
    permission_required = 'library.can_mark_returned'


class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    permission_required = 'library.can_mark_returned'




class CatalogCreate(PermissionRequiredMixin, CreateView):
    model = Catalog
    fields = '__all__'
    permission_required = 'library.can_mark_returned'


class CatalogUpdate(PermissionRequiredMixin, UpdateView):
    model = Catalog
    fields = '__all__'
    permission_required = 'library.can_mark_returned'


class CatalogDelete(PermissionRequiredMixin, DeleteView):
    model = Catalog
    success_url = reverse_lazy('catalogs')
    permission_required = 'library.can_mark_returned'