from django.shortcuts import render, redirect
from django.utils import timezone
from board.models import Book
from .forms import BookForm


# Create your views here.


def main(request):
    return render(request, 'board/main.html')


def posts(request):
    books = Book.objects.order_by('-create_dt')
    context = {'books': books}
    return render(request, 'board/board_posts.html', context)


def write(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.create_dt = timezone.now()
            book.save()
            return redirect('/board')
    else:
        form = BookForm()
        context = {'form': form}
        return render(request, 'board/board_write.html', context)
    context = {'form': form}
    print(form['title'])
    print(form.errors)
    return render(request, 'board/board_write.html', context)
