from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView

from .serializers import BooksSerializer, UserSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .models import *

from rest_framework.views import APIView
from rest_framework.decorators import api_view

class ListBookView(ListView):
    model = Book

    def get(self, request, *args, **kwargs):
        template_name = "books/list-books.html"  # sẽ được tạo ở phần dưới
        obj = {"books": Book.objects.all()}
        return render(request, template_name, obj)


# Create your views here.

class UserRegisterView(APIView):
    permission_classes = []
    def get_queryset(self):
        return User.objects.all()  # Adjust the queryset based on your needs

    # def get(self, request):
    #     queryset = self.get_queryset()
    #     # Your logic for handling GET requests (if needed)

    #     return JsonResponse({
    #         'message': 'This is the registration page.',
    #     })
    
    # def get(self, request):
    #     # Your logic for handling GET requests (if needed)
    #     return JsonResponse({
    #         'message': 'This is the registration page.',
    #     })
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            user = serializer.save()
            
            return JsonResponse({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)

        else:
            return JsonResponse({
                'error_message': 'This email has already exist!',
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
@csrf_exempt
@api_view(['GET', 'POST'])
def book_list(request, format=None):
   
    # if request.method == 'GET':
    #     books = Book.objects.all()
    #     serializer =BooksSerializer(books, many=True)
    #     return JsonResponse(serializer.data, safe=False)

    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = BooksSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)
    if request.method == 'GET':
        books = Book.objects.all()
        serializer =BooksSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BooksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BooksSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BooksSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 