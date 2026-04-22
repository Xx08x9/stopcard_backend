from django.http import JsonResponse
from .models import Product, CartItem
import json

def products(request):
    data = list(Product.objects.values())
    return JsonResponse(data, safe=False)

def add_to_cart(request):
    if request.method == "POST":
        data = json.loads(request.body)

        product = Product.objects.get(id=data["id"])
        CartItem.objects.create(product=product, quantity=1)

        return JsonResponse({"status": "added"})
    def cart(request):
    items = CartItem.objects.all()

    data = []
    for i in items:
        data.append({
            "name": i.product.name,
            "price": i.product.price,
            "quantity": i.quantity
        })

    return JsonResponse(data, safe=False)