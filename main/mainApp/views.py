from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import DeviceForm

from .models import *


class DeviceCreate(View):
    def get(self, request):
        form = DeviceForm
        return render(request, 'device_create.html', context={'form':form})

    def device(self, request):
        bound_form = DeviceForm(request.POST)
        if bound_form.is_valid():
            new_device = bound_form.save()
            return redirect(new_device)
        return render(request, 'device_create.html', context={'form':bound_form})


def device_list(request, category_slug = None):

    category = None
    categories = Category.objects.all()
    devices = Device.objects.all()

    paginator = Paginator(devices, 1)  # Show 5 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        devices = Device.objects.filter(category=category)

        paginator = Paginator(devices, 1)  # Show 5 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    return render(request,
                  'device_list.html',
                  {'category': category,
                   'categories': categories,
                   'devices': devices,
                   'page_obj':page_obj})


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
