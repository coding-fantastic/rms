"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# start of extensions need for image to show if debug is false
from django.urls import re_path as url, re_path

from django.conf import settings

from django.views.static import serve
# end of extensions need for image to show if debug is false

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include , re_path
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import RedirectView
from django.contrib import admin 


admin.site.site_header = 'Site Admin'
admin.site.site_title = 'Site Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('auth/', obtain_auth_token),

    # Catch-all pattern for undefined URLs
    re_path(r'^.*/$', RedirectView.as_view(url='/')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve,
                        {'document_root': settings.MEDIA_ROOT, }), ]
urlpatterns += [re_path(r'^static/(?P<path>.*)$', serve,
                        {'document_root': settings.MEDIA_ROOT, }), ]
