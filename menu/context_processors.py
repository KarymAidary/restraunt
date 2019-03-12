from .models import Basket


def getting_basket_count(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    try:
        basket = Basket.objects.get(session_key=session_key)
        dishes_count = basket.dishes.count()
    except:
        dishes_count = 0
    return locals()