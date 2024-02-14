import os

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
        context = {'form': form, 'page_for': '글 작성'}
        return render(request, 'board/board_write.html', context)
    context = {'form': form}
    return render(request, 'board/board_write.html', context)


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'DELETE':
        book.delete()
        return redirect('posts')
    context = {'book': book}
    return render(request, 'board/board_detail.html', context)


def rewrite(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    image_path = book.book_image.path
    if request.method == 'POST':
        # 기본값은 이전에 저장된 값으로 사용하고 만약 새로운 값이 입력되면 기본값에 덮어씌우는 방식으로 폼을 생성
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            if len(request.FILES) == 1 and os.path.exists(image_path):
                os.remove(image_path)
            book = form.save(commit=False)
            book.modify_dt = timezone.now()
            book.save()
            return redirect('posts')
    else:
        form = BookForm(instance=book)
    context = {'form': form, 'page_for': '글 수정', 'book_id': book_id}
    return render(request, 'board/board_rewrite.html', context)
