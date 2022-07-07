from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class CategoryView(APIView):

    def get(self, request):
        user_count = Category.objects.all()
        serializer = CategorySerializer(user_count,many=True)

        content = {'category': serializer.data}
        return Response({'category': content})


        # return Response(content)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message': 'user registration success'})


class ProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message': 'user registration success'})


def index(request):
    return render(request, 'index.html')