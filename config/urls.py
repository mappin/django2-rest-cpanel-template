"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# pylint: disable=C0103,E0401
from django.contrib import admin  #
from django.urls import include, path  #
from django.conf import settings  #
from django.conf.urls.static import static  #
from django.utils.translation import ugettext_lazy as _  #

from baseapp.views import (
    custom_400_error,
    custom_403_error,
    custom_404_error,
    custom_500_error,
)

admin.site.index_title = _('your admin index title')
admin.site.site_title = _('your site title')
admin.site.site_header = _('your site header')

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('__baseapp__/', include('baseapp.urls', namespace='baseapp'))
]

# Debug
'''
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))] + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    # for local development only...
    urlpatterns += [
        path('400/', custom_400_error),
        path('403/', custom_403_error),
        path('404/', custom_404_error),
        path('500/', custom_500_error),
    ]
'''
# Add your newly created app's urls here!
urlpatterns += [
    #path('', include('basemap.urls')),  # Go to main app urls
]

handler400 = custom_400_error
handler403 = custom_403_error
handler404 = custom_404_error
handler500 = custom_500_error
