from django.shortcuts import render, redirect
from e_commerce.models import *


# Create your views here.
def home(request):
    return render(request, 'store/home.html')


def store(request):
    cookie_number = len(request.COOKIES)
    context = {"products": ProductsModel.objects.all(), "cookie":cookie_number}
    return render(request, 'store/store.html', context)


def cart(request):

    #if request.user.is_authenticated:
    #   customer = request.user.customer
    #   order, created = OrderModel.objects.get_or_create(customer=customer, complete=False)
    #    items = order.orderitem_set.all()
    #else:
    #    items = []
    items = OrderItemModel.objects.all()
    orders = OrderModel.objects.all()
    context = {"items": items, "order":orders}
    return render(request, 'store/cart.html', context)


def checkout(request):
    items = OrderItemModel.objects.all()
    orders = OrderModel.objects.all()
    context = {"items": items, "order": orders}
    return render(request, 'store/checkout.html', context)


