from django.contrib import admin
from django.urls import path

from fictional.vehicles.views import ModelsViewSet, collection_conf, detail_conf, ModelSalesView, sales_conf
from fictional.sales.views import SalesViewSet, collection_conf as sale_conf

urlpatterns = [
    path(r'admin/', admin.site.urls),

    path(r'models/<int:pk>', ModelsViewSet.as_view(detail_conf)),
    path(r'models/<int:pk>/sales>', ModelSalesView.as_view(sales_conf)),
    path(r'models/', ModelsViewSet.as_view(collection_conf)),

    path(r'sales/', SalesViewSet.as_view(sale_conf))
]
