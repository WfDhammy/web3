from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login 
from .models import Product, Payment, Category, CartItem, Cart, Brand, LoginForm


def main(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    return render(request, 'index.html', {'products': products, 'categories': categories, 'brands':brands})


def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'details.html', {'product': product})

def login(request):
     if request.method == "POST":  
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                form.add_error(None, "Invalid username or password.")
        else:
            form = LoginForm()
   
    return render(request, 'auth.html', {'form': form})


