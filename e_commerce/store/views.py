from itertools import product
from math import prod
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view


class CategoryView(APIView):

    def get(self, request):
        category_obj = Category.objects.all()
        serializer = CategorySerializer(category_obj, many=True)
        return Response({'category': serializer.data})

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message': 'user registration success'})


class ProductView(APIView):
    def get(self, request):
        product_obj = Product.objects.all()
        serializer = ProductSerializer(product_obj, many=True)
        return Response({'category': serializer.data})


class CartView(APIView):
    def post(self, request):
        product = request.POST['product']
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart']=cart
        print(cart)
        # print(request.POST[''])
        # serializer = ProductSerializer(obj, many=True)
        return Response({'status': 200, })


def index(request):
    return render(request, 'index.html')


def login_page(request):
    return render(request, 'login.html')


def signup_page(request):
    return render(request, 'signup.html')


@csrf_exempt
@api_view(["POST"])
def filter_product(request):

    # if request.POST[]
    # obj = Product.objects.filter(category='Dress').values
    print(request.POST['aa'])
    # serializer = ProductSerializer(obj, many=True)
    return Response({'status': 200, })
