from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book
from .forms import ReviewForm
import datetime

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {"books": books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    reviews = book.reviews.order_by("-created_at")
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.full_clean()
            review.save()
            return redirect("book_detail", id=book.id)
    else:
        form = ReviewForm()
    return render(request, "books/book_detail.html", {"book": book, "reviews": reviews, "form": form})

def current_time(request):
    now = datetime.datetime.now()
    return HttpResponse(f"<h1>Текущее время: {now.strftime('%Y-%m-%d %H:%M:%S')}</h1>")
