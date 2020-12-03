from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'system'

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/<slug:category_slug>/', views.product_list_by_category, name='product_list_by_category'),
    path('catalog/<slug:category_slug>/<slug:subcategory_slug>/', views.product_list_by_subcategory, name='product_list_by_subcategory'),
    path('search/', views.global_search, name='global_search'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)