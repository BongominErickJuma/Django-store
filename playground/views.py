from django.shortcuts import render
from django.db.models import Q
from store.models import Product, Order



def sayHello(request):

    queryset = Order.objects.select_related("customer").prefetch_related("orderitem_set__product").order_by("-placed_at")
    return render(request, "hello.html",{ "products": list(queryset)})
