from django.shortcuts import render,get_object_or_404,redirect
from store.models import Meds
from .models import CartItems,Cart
# from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from accounts.models import UserProfile


# @login_required
def viewCart(request):
    user , _ = UserProfile.objects.get_or_create(user = request.user)
    cart , created = Cart.objects.get_or_create( user = user)
    cart_items = cart.items.all().select_related('product') 
    total_price = cart_items.aggregate(total = Sum(F('quantity') * F('product__price'))) ['total'] or 0
    context = {
        'cart_items' : cart_items, 
        'total_price' : total_price,
    }
    return render(request , 'view_cart.html', context)

# @login_required
def addToCart(request , pk):
    med = get_object_or_404(Meds ,pk = pk)
    user , _ = UserProfile.objects.get_or_create(user = request.user)
    cart , _ = Cart.objects.get_or_create(user=user)
    cart_item, created = CartItems.objects.get_or_create (cart = cart , product = med)
    if not created: 
        cart_item.quantity += 1 
        cart_item.save()
    return redirect ('home')

def updateCartItem(request, pk):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItems, pk=pk)
        action = request.POST.get('action')
        
        if action == 'increase':
            if cart_item.quantity < cart_item.product.qty:  
                cart_item.quantity += 1
                cart_item.save()
        elif action == 'decrease':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else :
                cart_item.delete()

    return redirect('vcart')

def removeCartItem (request , pk): 
    item = get_object_or_404(CartItems , pk = pk )
    item.delete()
    return redirect('vcart')
