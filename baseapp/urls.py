from django.urls import path

from .views import views  #

app_name = 'baseapp'   # namespacing of dynamically reference URLs.

urlpatterns = [
    path(path('', views.homepage, name='homepage')
    ] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
