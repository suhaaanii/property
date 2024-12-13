# product/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

# Display all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'prodcut_list.html', {'products': products})

# Display a single product
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

# Add a new product
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list after creating a product
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})
