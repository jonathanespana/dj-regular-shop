from .models import Cart

def cart_renderer(request):
    try:
        cart = Cart.objects.get(session_id = request.session['nonuser'], completed=False)

    except:
        cart = {"num_of_items": 0}

    return {"cart": cart}