from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductForm



# Create your views here.
class ProductListView(ListView):
    queryset = Product.objects.all().order_by("-timestamp")
    paginate_by = 10
    template_name = 'list.html'


class MyProductListView(ListView):
    paginate_by = 10
    template_name = 'list.html'

    def get_queryset(self):
        q = Product.objects.filter(user__user__username__iexact=self.request.user.username).order_by("-timestamp")
        return q


def detail(request, pk):
    context = {}
    product = get_object_or_404(Product, pk=pk)
    context['object'] = product
    return render(request, "single.html", context)


class Traditional(ListView):
    queryset = Product.objects.filter(category__iexact="traditional").order_by("-timestamp")
    paginate_by = 10
    template_name = 'list.html'


# Products CreateView
@login_required
def create(request, template_name='post.html' ):
    form = ProductForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.user = request.user.profile
        f.save()
        return redirect('products')
    else:
        messages.error(request, 'Please correct the error below')
        form = ProductForm()
    return render(request, template_name, {'form': form})


# Product EditView
@login_required
def edit(request, pk):
    template = 'post.html'
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None,request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        messages.success(request, 'Succesfully Edited')
        return redirect('myproducts')
    return render(request, template, {'form': form})


@login_required
def delete(request, pk):
    template = 'delete.html'
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('myproducts')
    return render(request, template, {'object': product})


class Formal(ListView):
    queryset = Product.objects.filter(category__iexact="formal").order_by("-timestamp")
    paginate_by = 10
    template_name = 'list.html'

class Casual(ListView):
    queryset = Product.objects.filter(category__iexact="casual").order_by("-timestamp")
    paginate_by = 10
    template_name = 'list.html'

class Ethnic(ListView):
    queryset = Product.objects.filter(category__iexact="ethnic").order_by("-timestamp")
    paginate_by = 10
    template_name = 'list.html'

class Sports(ListView):
    queryset = Product.objects.filter(category__iexact="sport").order_by("-timestamp")
    paginate_by = 10
    template_name = 'list.html'

class Western(ListView):
    queryset = Product.objects.filter(category__iexact="western").order_by("-timestamp")
    paginate_by = 10
    template_name = 'list.html'

class Tshirts(ListView):
    queryset = Product.objects.filter(category__iexact="t-shirts").order_by("-timestamp")
    paginate_by = 10
    template_name = 'list.html'

class Kids(ListView):
    queryset = Product.objects.filter(category__iexact="kids").order_by("-timestamp")
    paginate_by = 10
    template_name = 'list.html'

class Jumpsuits(ListView):
    queryset = Product.objects.filter(category__iexact="jumpsuits").order_by("-timestamp")
    paginate_by = 10
    template_name = 'list.html'

class Denim(ListView):
    queryset = Product.objects.filter(category__iexact="denim").order_by("-timestamp")
    paginate_by = 10
    template_name = 'list.html'

