from django.urls import path

from books import views

app_name = 'books'
urlpatterns = [
    path('', views.BookListView.as_view(), name='books_list'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
]