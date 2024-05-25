from django.shortcuts import render, redirect
from .models import Product, Order
from .forms import ProductForm
from django.http import HttpResponse

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Product

def generate_report(request):
    
    products = Product.objects.all()

   
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="warehouse_report.pdf"'

    
    p = canvas.Canvas(response)
    p.drawString(100, 800, 'Warehouse Report')
    y = 750
    for product in products:
        y -= 20
        p.drawString(100, y, f"Product Name: {product.name}")
        p.drawString(100, y - 10, f"Quantity: {product.quantity}")
        p.drawString(100, y - 20, f"Description: {product.description}")
        p.drawString(100, y - 30, f"Cost: {product.cost} rs.")
    p.showPage()
    p.save()

    return response
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})



def remove_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('index')

def home(request):
    if request.method == 'POST':
        if 'order' in request.POST:
            product_id = request.POST.get('product_id')
            product = Product.objects.get(id=product_id)
            Order.objects.create(product=product, status='registered')
            return redirect('home')
        elif 'remove_order' in request.POST:
            order_id = request.POST.get('order_id')
            Order.objects.get(id=order_id).delete()
            return redirect('home')
    else:
        products = Product.objects.all()
        orders = Order.objects.all()
        return render(request, 'home.html', {'products': products, 'orders': orders})

def index(request):
    if request.method == 'POST' and 'collect_order' in request.POST:
        order_id = request.POST.get('order_id')
        order = Order.objects.get(id=order_id)
        order.status = 'collected'
        order.save()
        return redirect('index')
    else:
        orders = Order.objects.filter(status='registered')
        return render(request, 'index.html', {'orders': orders})

def search_results(request):
    search_query = request.GET.get('search_query')
    
    if search_query:
        products = Product.objects.filter(name__icontains=search_query)
    else:
        products = Product.objects.none()
    
    return render(request, 'search_results.html', {'products': products, 'search_query': search_query})