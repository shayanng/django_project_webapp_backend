from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer


# class Another(View):
#
#     books = Book.objects.all()
#     output = ""
#     for book in books:
#
#         output += f"We have {book.title} book with ID {book.id} Data Base.<br>"
#
#     def get(self, request):
#         return HttpResponse(self.output)


# Create your views here.
# def first(request):
#     return HttpResponse("first message from views")

def first(request):
    books = Book.objects.all()

    return render(request, "temp1.html", {"books": books})


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
