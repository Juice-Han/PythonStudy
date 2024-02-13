from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from board.models import Book
from .forms import BookForm


# Create your views here.


def main(request):
    return render(request, 'board/main.html')


def posts(request):
    books = Book.objects.order_by('-create_dt')
    for book in books:
        if len(book.content) > 50:
            book.content = ''.join([book.content[:50], '...'])
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


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    return render(request, 'board/board_detail.html', context)
