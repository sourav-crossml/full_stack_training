import email
from urllib import response
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import *
# Create your views here.
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


class Registeruser(APIView):
    """
    wsad
    """

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})
            
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({'status': 200, 'payload': serializer.data,  'refresh': str(refresh), 'access': str(refresh.access_token), 'message': 'user registration success'})

from django.contrib.auth import authenticate, login

@api_view(["POST"])
@permission_classes([AllowAny])

def login_user(request):
    username = request.POST['email']
    print(username)
    password = request.POST['password']
    print(password)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'status': 200,})
        # Redirect to a success page.
        ...
    else:
        return Response({'status': 404,})
        # Return an 'invalid login' error message.
        ...

# def login_user(request):

#     data = {}
#     # breakpoint()
#     reqBody = str(request.body)
#     x = reqBody.replace("&", ",")
#     res = dict(item.split("=") for item in x.split(","))
#     print(res)
#     email1 = res['email']

#     print(email1)
#     password = res['password']
#     password = password.replace("'", "")
#     print(password)
#     try:

#         Account = User.objects.filter(email=email1)
#     except BaseException as e:
#         raise ValidationError({"400": f'{str(e)}'})

#     token = Token.objects.get_or_create(user=Account)[0].key
#     print(token)
#     if not check_password(password, Account.password):
#         raise ValidationError({"message": "Incorrect Login credentials"})

#     if Account:
#         if Account.is_active:
#             print(request.user)
#             login(request, Account)
#             data["message"] = "user logged in"
#             data["email"] = Account.email

#             Res = {"data": data, "token": token}

#             return Response(Res)

#         else:
#             raise ValidationError({"400": f'Account not active'})

#     else:
#         raise ValidationError({"400": f'Account doesnt exist'})
