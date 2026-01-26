from django.conf import settings

def cart_count(request):
    """
    Adds the number of items in the user's cart to the context.
    """
    cart = request.session.get('cart', {})
    return {
        'cart_count': sum(cart.values()) if isinstance(cart, dict) else 0
    }
