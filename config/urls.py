from django.contrib import admin
from django.urls import path

from fictional.vehicles.views import ModelViewSet, collection_conf, detail_conf, ModelSalesView, sales_conf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('models/<int:pk>', ModelViewSet.as_view(detail_conf)),
    path('models/<int:pk>/sales>', ModelSalesView.as_view(sales_conf)),
    path('models/', ModelViewSet.as_view(collection_conf))

]
