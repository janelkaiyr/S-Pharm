from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
                  path('', views.index, name='main'),
                  path('index', views.index2, name='main2'),
                  path('delivery', views.Delivery, name='del'),
                  path('drugs', views.drugs, name='all_drug'),
                  path('analog', views.analogies, name='analog'),
                  path('partner', views.model_form_upload, name='partner'),
                  path('recom', views.recommendations, name='recommend'),
                  path('map', views.map, name='map'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
