from django.http import JsonResponse
from .models import Product

def product_list(request):
    products = list(Product.objects.values('id', 'name', 'price'))
    return JsonResponse(products, safe=False)

def api_root(request):
    return JsonResponse({"message": "API Casio.kg"})

def get_cart(request):
    cart = request.session.get('cart', {})
    data = []
    total_sum = 0
    for pid, qty in cart.items():
        product = Product.objects.filter(id=pid).first()
        if product:
            item_total = product.price * qty
            total_sum += item_total
            data.append({
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "quantity": qty,
                "total": item_total
            })
    return JsonResponse({"items": data, "total_price": total_sum})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    pid = str(product_id)
    cart[pid] = cart.get(pid, 0) + 1
    request.session['cart'] = cart
    return JsonResponse({"message": "Added"})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    pid = str(product_id)
    if pid in cart:
        del cart[pid]
    request.session['cart'] = cart
    return JsonResponse({"message": "Removed"})

def clear_cart(request):
    request.session['cart'] = {}
    return JsonResponse({"message": "Cleared"})