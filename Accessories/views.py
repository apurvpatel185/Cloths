from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from .models import Accessories
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AccessoriesForm

# Create your views here.

class AccessoriesListView(ListView):
    queryset = Accessories.objects.all().order_by("-timestamp")
    paginate_by = 10
    template_name = 'list.html'


def type1(request):
    template = "type1.html"
    return render(request, template, {})


def detail(request, slug):
    context = {}
    accessories = get_object_or_404(Accessories, slug=slug)
    context['object'] = accessories
    return render(request, "single.html", context)


# Products CreateView
@login_required
def create(request, template_name='post.html'):
    form = AccessoriesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.user = request.user.profile
        f.save()
        return redirect('accessories')
    else:
        messages.error(request, 'Please correct the error below')
        form = AccessoriesForm()
    return render(request, template_name, {'form': form})


# Product EditView
@login_required
def edit(request, pk):
    template = 'post.html'
    accessories = get_object_or_404(Accessories, pk=pk)
    form = AccessoriesForm(request.POST or None,request.FILES or None, instance=accessories)
    if form.is_valid():
        form.save()
        messages.success(request, 'Succesfully Edited')
        return redirect('myproducts')
    return render(request, template, {'form': form})


@login_required
def delete(request, pk):
    template = 'delete.html'
    accessories = get_object_or_404(Accessories, pk=pk)
    if request.method == 'POST':
        accessories.delete()
        return redirect('myaccessories')
    return render(request, template, {'object': accessories})


class Cap(ListView):
    queryset = Accessories.objects.filter(category__iexact="cap").order_by("-timestamp")
    paginate_by = 10
    template_name = 'list.html'


class Tie(ListView):
    queryset = Accessories.objects.filter(category__iexact="tie").order_by("-timestamp")
    paginate_by = 10
    template_name = 'list.html'


class Brooch(ListView):
    queryset = Accessories.objects.filter(category__iexact="brooch").order_by("-timestamp")
    paginate_by = 10
    template_name = 'list.html'


class Jewellary(ListView):
    queryset = Accessories.objects.filter(category__iexact="jewellary").order_by("-timestamp")
    paginate_by = 10
    template_name = 'list.html'


class Wig(ListView):
    queryset = Accessories.objects.filter(category__iexact="wig").order_by("-timestamp")
    paginate_by = 10
    template_name = 'list.html'


class Purse(ListView):
    queryset = Accessories.objects.filter(category__iexact="purse").order_by("-timestamp")
    paginate_by = 10
    template_name = 'list.html'


class SearchList(ListView):
    paginate_by = 10
    template_name = 'list.html'

    def get_queryset(self):
        q = self.request.GET.get("product", None)
        if q is not None:
            sell = Accessories.objects.filter(
                Q(title__icontains=q) |
                Q(description__icontains=q) |
                Q(category__iexact=q)
            )
            return sell


class SearchList1(ListView):
    paginate_by = 10
    template_name = 'list.html'

    def get_queryset(self):
        q = self.request.GET.get("product", None)
        q1 = self.request.GET.get("category", None)
        if q and q1 is not None:
            sell = Accessories.objects.filter(
                Q(title_icontains=q) | Q(description_icontains=q) &
                Q(category__iexact=q1)
            )
            return sell


class Men(ListView):
    queryset = Accessories.objects.filter(gender__iexact="M").order_by("-timestamp")
    paginate_by = 10
    template_name = 'list.html'


class Women(ListView):
    queryset = Accessories.objects.filter(gender__iexact="F").order_by("-timestamp")
    paginate_by = 10
    template_name = 'list.html'


