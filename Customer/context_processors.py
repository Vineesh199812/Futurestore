from Owner.models import Carts


def cart_count(request):
    user=request.user
    cnt = Carts.objects.filter(user=user, status="in-cart").count()
    return {"cnt": cnt}
