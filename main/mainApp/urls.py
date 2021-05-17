from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('device_list/', views.device_list, name='device_list'),
    path('device/create', views.DeviceCreate.as_view(), name='device_create'),
    path('device/<str:device_slug>', views.device_item, name='device_item'),
    re_path(r'^category/(?P<category_slug>[-\w]+)/$', views.device_list,
            name='device_list_by_category'),
    path('search/', views.search_result, name='search_result')
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
