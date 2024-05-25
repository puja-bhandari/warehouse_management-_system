
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('add_product/', views.add_product, name="add_product"),
    path('remove/',views.remove_product, name='remove_product'),
    path('', views.home , name='home'),
     path('search/',views.search_results, name='search_results'),
path('generate-report/', views.generate_report, name='generate_report'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)