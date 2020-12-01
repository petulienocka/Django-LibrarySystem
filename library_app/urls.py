from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'), 
    path('catalogs/', views.CatalogListView.as_view(), name='catalogs'),
    path('catalog/<int:pk>', views.CatalogDetailView.as_view(), name='catalog-detail'),
]

urlpatterns += [   
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed-books'),
    path(r'borrowedbooks/', views.LoanedBooksAllListView.as_view(), name='all-borrowed-books'),
  
]

urlpatterns += [   
    path('mycatalogs/', views.LoanedCatalogsByUserListView.as_view(), name='my-borrowed-catalogs'),
    path(r'borrowedcatalogs/', views.LoanedCatalogsAllListView.as_view(), name='all-borrowed-catalogs'),   
]

urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]

urlpatterns += [
    path('catalog/<uuid:pk>/renew/', views.renew_catalog_librarian, name='renew-catalog-librarian'),
]

urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]

urlpatterns += [
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]

urlpatterns += [
    path('catalog/create/', views.CatalogCreate.as_view(), name='catalog_create'),
    path('catalog/<int:pk>/update/', views.CatalogUpdate.as_view(), name='catalog_update'),
    path('catalog/<int:pk>/delete/', views.CatalogDelete.as_view(), name='catalog_delete'),
]
