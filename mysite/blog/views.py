from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from blog.models import Author, Books
from blog.forms import BookForm, AuthorForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.db.models import Q


# Create your views here.


# index page Fot Books
def index(request):
    text = Books.objects.all()
    query = request.GET.get("q")
    # search bar
    if query:
        text = text.filter(
            Q(Author__first_name__icontains=query) |
            Q(Author__last_name__icontains=query)
        )
    return render(request, 'blog/index.html', {"text": text})

# index page Fot Authors


def index_auth(request):
    text = Author.objects.all()
    query = request.GET.get('q')
    if query:
        text = text.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )

    return render(request, 'blog/auth_index.html', {"text": text})

# details page for books


def book_detail(request, pk):
    book = get_object_or_404(Books, pk=pk)
    return render(request, 'blog/book_detail.html', {'book': book})


# details page for Authors
def auth_detail(request, pk):
    auth = get_object_or_404(Author, pk=pk)
    return render(request, 'blog/auth_detail.html', {'auth': auth})


# insert new book page
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')

    else:
        form = BookForm()
    return render(request, 'blog/add_book.html', {'form': form})


# insert new Author
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index_auth')

    else:
        form = AuthorForm()
    return render(request, 'blog/add_author.html', {'form': form})


# update Book
def book_update(request, pk, template_name='book_edit.html'):

    book = get_object_or_404(Books, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'blog/book_edit.html', {'form': form})


# update Author
def auth_update(request, pk, template_name='book_edit.html'):

    auth = get_object_or_404(Author, pk=pk)
    form = AuthorForm(request.POST or None, instance=auth)
    if form.is_valid():
        form.save()
        return redirect('index_auth')
    return render(request, 'blog/book_edit.html', {'form': form})

# search bar


def article_overview(request):
    search_term = ''

    if 'search' in request.GET:
        search_term = request.GET['search']
        books = Books.objects.all().filter(feeder__icontains=search_term)

    books = Books.objects.all()

    return render(request, 'blog/index.html', {'Books': books, 'search_term': search_term})


# Delete Books
def book_delete(request, pk, template_name='book_confirm_delete.html'):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('index')
    return render(request, 'blog/book_confirm_delete.html', {'object': book})


# Delete Authors
def auth_delete(request, pk, template_name='book_confirm_delete.html'):
    auth = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        auth.delete()
        return redirect('index_auth')
    return render(request, 'blog/book_confirm_delete.html', {'object': auth})

# search Box
