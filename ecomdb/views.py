from django.http import response
from django.shortcuts import render
# from rest_framework import generics

from rest_framework.response import Response
from rest_framework.serializers import Serializer

from .models import Product
from .serializers import ProductSerializer
from .forms import Product_form, Choose_form

from rest_framework.decorators import api_view  

from django.http import HttpResponse

def home(request):
    form = Choose_form()

    if 'POST' == request.method:
        form = Choose_form(request.POST)

    context = {
        'form' : form
    }
    return render(request, 'ecomdb/home.html', context)

#--------API Views--------#
@api_view(['GET'])
def productList(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    context = {
        'products' : serializer.data
    }

    return render(request,'ecomdb/List_view.html', context)
    # return Response(serializer.django Method Not Allowed: /url -POST -GETdata) <---Old way.

@api_view(['GET'])
def productDetail(request,pk):

    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist :
        return HttpResponse("<h2> There is no stored product with id = %i. Please try another Id.<a href=\"localhost:8000/list\"> List of products </a></h2>" % pk)

    serializer = ProductSerializer(product)

    context = {
        'product' : serializer.data
    }

    return render(request,'ecomdb/Detail_view.html', context)


@api_view(['GET','POST'])
def productAdd(request):

    if 'POST' == request.method:
        form = Product_form(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            quantiy = form.cleaned_data['quantity']

            product = Product(name=name,price=price,quantity=quantiy)
            product.save()
            
    else:
        form = Product_form()


    context = {
        'form' : form
    }
    
    return render(request, 'ecomdb/Add_view.html', context)

@api_view(['GET','POST'])
def productUpdate(request,pk):
    product = Product.objects.get(id=pk)
    serializer_old = ProductSerializer(product)

    if 'POST' == request.method:
        form = Product_form(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            quantiy = form.cleaned_data['quantity']
            id = pk

            product = Product(id,name,price,quantiy)
            product.save()
            
    else:
        form = Product_form()

    context = {
        'product' : serializer_old.data,
        'form' : form
    }
    
    return render(request, 'ecomdb/Update_view.html', context)

@api_view(['GET','DELETE'])
def productDeleteChoose(request,pk):
    try :
        product = Product.objects.get(id=pk)

        serializer = ProductSerializer(product)
        context = {
            'product' : serializer.data
        }
        print(request.method)
        return render(request, 'ecomdb/Delete_Choose_view.html',context)
    except Product.DoesNotExist :
        return HttpResponse("<h2> There is no stored product with id = %i. Please try another Id.<a href=\"localhost:8000/list\"> List of products </a></h2>" % pk)


@api_view(['GET','POST','DELETE'])
def productDeleted(request,pk):

    try:
        product = Product.objects.get(id=pk)
        product.delete()
        context = {
        'id' : pk
        }
        return render(request, 'ecomdb/Deleted_view.html', context)

    except Product.DoesNotExist :
        return HttpResponse("<h2> There is no stored product with id = %i. Please try another Id.<a href=\"localhost:8000/list\"> List of products </a></h2>" % pk)

