from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist  # used for try catch
from django.db.models import Q, F, Value, ExpressionWrapper
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models.fields import DecimalField
from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from store.models import Product, OrderItem, Customer, Collection, Order
from tags.models import TaggedItem


# Create your views here.


def say_hello(request):
    # ...

    with transaction.atomic():
        order = Order()
        order.customer_id = 1
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 1
        item.unit_price = 5
        item.save()

    return render(request, "hello.html", {"name": "Karl"})
