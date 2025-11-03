from django.shortcuts import render
from .models import Book
from .forms import UserForm  # type: ignore


def book_list(request):
    books = Book.objects.all()  # ORM query
    return render(request, "bookapp/books.html", {"books": books})


def user_form(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            return render(
                request, "bookapp/submitted.html", {"name": name, "email": email}
            )
    else:
        form = UserForm()
    return render(request, "bookapp/form.html", {"form": form})
