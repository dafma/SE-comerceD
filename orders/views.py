from django.shortcuts import render
from .models import OrderItem
from .forms import OrdenCreateForm
from cart.cart import Cart
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import  reverse
# Create your views here.
from  .tasks import order_created
from django.contrib.admin.views.decorators import  staff_member_required
from .models import Orden
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
#import weasyprint


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Orden, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order':order,})


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrdenCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
                order.save()
            for item in cart:
                OrderItem.objects.create(
                                        orden=order,
                                        product=item['product'],
                                        precio=item['price'],
                                        cantidad=item['quantity'],
                )
            #limpiamos l carro
            cart.clear()
            #lanzamos el proceso asincrono
            order_created.delay(order.id)
            #set the order in the session
            request.session['order_id'] = order.id
            #redirect to the payment
            return redirect(reverse('payment:process'))

    else:
        form = OrdenCreateForm()
    return render(request, 'orders/order/created.html', {'cart':cart, 'form':form})
