from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import DeviceForm
from .models import *


class DeviceCreate(View):

    def get(self, request):
        form = DeviceForm
        return render(request, 'device_create.html', context={'form': form})

    def post(self, request):
        bound_form = DeviceForm(request.POST)
        if bound_form.is_valid():
            new_device = bound_form.save()
            return redirect(new_device)
        return render(request, 'device_create.html', context={'form': bound_form})


def device_list(request, category_slug=None):

    category = None
    categories = Category.objects.all()
    devices = Device.objects.all()

    # coordinate filter data
    s1x = request.GET.get('s1x', 0)
    s1y = request.GET.get('s1y', 0)
    s2x = request.GET.get('s2x', 0)
    s2y = request.GET.get('s2y', 0)

    # radius filter data
    r1 = request.GET.get('r1', 0)
    r2 = request.GET.get('r2', 0)

    # category filter
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        devices = devices.filter(category=category)

    # coordinate filter
    if s1x != '' and s2x != '' and s1y != '' and s2y != '' and s1y != 0 and s2y != 0:
        devices = devices.filter(latitude__range=(s1x, s2x), longitude__range=(s1y, s2y))

    # radius filter
    if r2 != 0 and r1 != '' and r2 != '':
        devices = devices.filter(radius__range=(r1, r2))

    paginator = Paginator(devices, 2)  # Show n contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,
                  'device_list.html',
                  {'category': category,
                   'categories': categories,
                   'devices': devices,
                   'page_obj': page_obj})


def device_item(request, device_slug):
    device = get_object_or_404(Device,
                               slug=device_slug)
    return render(request, 'device_item.html', {'device': device, })


def index(request):
    return render(request, 'index.html', {})


def search_result(request):
    query = request.GET.get('q')
    object_list = Device.objects.filter(
        Q(name__icontains=query) | Q(address__icontains=query)
    )

    context = {
        'items': object_list
    }
    return render(request, 'search_result.html', context)
