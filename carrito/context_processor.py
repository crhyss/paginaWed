from django.contrib.auth.models import User
def monto_total_cart(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session['cart']:
            total = total + (int(value['precio']) * value['cantidad'])
    return {'monto_total_cart': total}