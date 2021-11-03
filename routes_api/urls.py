from django.urls import path
from .views import TruckRouteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('trucks/', TruckRouteView.as_view(), name='trucks_list')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)