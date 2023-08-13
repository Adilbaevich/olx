from django.shortcuts import render, redirect
from .models import Product
from .models import Product1
from .models import Product2
from .models import Product3
from .models import Product4
from django.http import Http404
from django.contrib.auth.decorators import login_required

from .forms import ProductForm
from .forms import Product3Form
from .forms import Product2Form
from .forms import Product4Form



def home(request):
    return render(request,'base.html')


def animal(request):
    products3 = Product3.objects.all()
    context = {
        'products3': products3
    }
    return render(
        request,
        'pages/animal.html',
        context
    )
@login_required(redirect_field_name='login')
def animal_detail(request,pk):
    try:
        product3 = Product3.objects.get(id=pk)
    except Product3.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'product3': product3
    }

    return render(request, 'pages/animal_detail.html', context)

def create_animal(request):
    if request.method == 'POST':
        form = Product3Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(to='animal')
    else:
        form = Product3Form()
    context = {
        'form': form
    }
    return render(request,'pages/create.html', context)



def business_detail(request,pk):
    try:
        product1 = Product1.objects.get(id=pk)
    except Product1.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'product1': product1
    }

    return render(request, 'pages/business_detail.html', context)

def electro(request):
    products2 = Product2.objects.all()
    context = {
        'products2': products2
    }
    return render(
        request,
        'pages/electro.html',
        context
    )
@login_required(redirect_field_name='login')
def electro_detail(request,pk):
    try:
        product2 = Product2.objects.get(id=pk)
    except Product2.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'product2': product2
    }

    return render(request, 'pages/electro_detail.html', context)

def create(request):
    if request.method == 'POST':
        form = Product2Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(to='electro')
    else:
        form = Product2Form()
    context = {
        'form': form
    }
    return render(request,'pages/create.html', context)

def realty(request):
    return render(request, 'pages/realty.html')

def furnature(request):
    products4 = Product4.objects.all()
    context = {
        'products4': products4
    }
    return render(
        request,
        'pages/furnature.html',
        context
    )
@login_required(redirect_field_name='login')
def furnature_detail(request,pk):
    try:
        product4 = Product4.objects.get(id=pk)
    except Product4.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'product4': product4
    }

    return render(request, 'pages/furnature_detail.html', context)

def create_furnature(request):
    if request.method == 'POST':
        form = Product4Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(to='furnature')
    else:
        form = Product4Form()
    context = {
        'form': form
    }
    return render(request,'pages/create.html', context)

def transport(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(
        request,
        'pages/transport.html',
        context
    )

def create_transport(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(to='transport')
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request,'pages/create.html', context)

@login_required(redirect_field_name='login')
def transport_detail(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'product': product
    }

    return render(request, 'pages/transport_detail.html', context)

#*args, **kwargs


def transport_delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete() 
    return redirect(to='transport')


def transport_update(request,pk):
    product = Product.objects.get(id=pk)
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            author = form.cleaned_data['author']

            product.title = title
            product.image = image
            product.description = description
            product.price = price
            product.author = author
            product.save()

            return redirect(to='transport')
    context = {
        'form': form
    }
    return render(request, 'pages/update.html', context)
    


def animal_delete(request, pk):
    product3 = Product3.objects.get(id=pk)
    product3.delete() 
    return redirect(to='animal')


def animal_update(request,pk):
    product3 = Product3.objects.get(id=pk)
    form = Product3Form()
    if request.method == 'POST':
        form = Product3Form(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            author = form.cleaned_data['author']

            product3.title = title
            product3.image = image
            product3.description = description
            product3.price = price
            product3.author = author
            product3.save()

            return redirect(to='animal')
    context = {
        'form': form
    }
    return render(request, 'pages/update_animal.html', context)
    


def electro_delete(request, pk):
    product2 = Product2.objects.get(id=pk)
    product2.delete() 
    return redirect(to='electro')


def electro_update(request,pk):
    product2 = Product2.objects.get(id=pk)
    form = Product2Form()
    if request.method == 'POST':
        form = Product2Form(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            author = form.cleaned_data['author']

            product2.title = title
            product2.image = image
            product2.description = description
            product2.price = price
            product2.author = author
            product2.save()

            return redirect(to='electro')
    context = {
        'form': form
    }
    return render(request, 'pages/update_electro.html', context)
    
def furnature_delete(request, pk):
    product4 = Product4.objects.get(id=pk)
    product4.delete() 
    return redirect(to='furnature')


def furnature_update(request,pk):
    product4 = Product4.objects.get(id=pk)
    form = Product4Form()
    if request.method == 'POST':
        form = Product4Form(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            author = form.cleaned_data['author']

            product4.title = title
            product4.image = image
            product4.description = description
            product4.price = price
            product4.author = author
            product4.save()

            return redirect(to='furnature')
    context = {
        'form': form
    }
    return render(request, 'pages/update.html', context)