from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json

# Create your views here.
#..
def store(request):
#if condition tells  if user is logged in to website then what will be shown on that page
    if request.user.is_authenticated:
        customer = request.user.customer
        #below code says if order is placed then okay  else create a order
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        #cart items here is added to show no of items in cart shown on navbar
        cartitems =order.get_cart_items
#else if user is not logged in
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        #cart items here is added to show num of items in cart shown on navbar
        cartitems = order['get_cart_items']
    products=Product.objects.all() 
    context={'products':products , 'cartitems':cartitems}
    return render(request,'store/store.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0 , 'get_cart_items':0}
        cartitems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartitems': cartitems}
    return render(request, 'store/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartitems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartitems': cartitems}
    return render(request,'store/checkout.html',context)


    
def updateItem(request):
    #data is loading all the content that is updated in the body .
	data = json.loads(request.body)
    #loading data involves  product id and action
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)
    #json response is used when we dont have to return any template instead when we want to return any message.
