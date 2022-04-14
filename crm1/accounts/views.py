from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import *

def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	total_customers = customers.count()
	total_orders = orders.count()
	deliveried = orders.filter(status="Deliveried").count()
	pending = orders.filter(status ="Pending").count()

	context = {'orders': orders,'customers': customers,'total_orders': total_orders,
				'deliveried': deliveried,'pending':pending
				}
	return render(request, 'accounts/dashboard.html',context)

def products(request):
	products = Products.objects.all()
	return render(request, 'accounts/products.html', {'products': products})

def customer(request,pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	context = {'customer':customer, 'orders':orders,'order_count':order_count}
	return render(request, 'accounts/customer.html',context)

