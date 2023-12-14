import django.contrib.auth.models
from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Book, Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
import rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

# Using generic class-based views:
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import renderers
from rest_framework import viewsets
from django.contrib.auth.models import User

# ------------- Create an endpoint for root of our API:

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list',request=request,format=format),
#         'snippets': reverse('snippet-list',request=request,format=format)
#     })


from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from snippets.models import MyUser
from snippets.serializers import UserSerializer, UserLoginSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from snippets.serializers import BookSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """

    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LoginView(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                username=serializer.validated_data["username"],
                password=serializer.validated_data["password"],
            )
            if user:
                token, created = Token.objects.get_or_create(user=user)
                # refresh = TokenObtainPairSerializer.get_token(user)
                data = {"access_token": str(token), "user_id": str(user.id)}
                return Response(data, status=status.HTTP_200_OK)

        return Response(
            {"error_message": "Email or password is incorrect!", "error_code": 400},
            status=status.HTTP_400_BAD_REQUEST,
        )


class RegisterView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.validated_data("password")
            user = serializer.save()
            # user= MyUser.objects.create_user(email=request.data.username, password=request.data.password)
            # user.save();
            # return Response(request.data, status=status.HTTP_201_CREATED)
            return JsonResponse(
                {"message": "Register successful!"}, status=status.HTTP_201_CREATED
            )
        else:
            return JsonResponse(
                {
                    "error_message": "This email has already exist!",
                    "errors_code": 400,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class BookViewSet(viewsets.ModelViewSet):
    permissions_classes = [permissions.IsAuthenticated]
    # model = Book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
