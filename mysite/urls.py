from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.views.generic import TemplateView

# from filebrowser.sites import site

# from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('summernote/', include('django_summernote.urls')),

    path('myinfo/', include('myinfo.urls')),
    
    path('', RedirectView.as_view(url='/myinfo/')),
    # path('', include(tf_urls)),
    # # path('accounts/', include('two_factor.urls', namespace='two_factor')),
    
    # path('', include('myinfo.urls')),

    path('mysched/', include('mysched.urls')),
    # path('mycontact/', include('mycontact.urls')),
    path('sample/', include('sample.urls')),
    path('myreport/', include('myreport.urls')),

    # path('admin/filebrowser/', site.urls),
    # path('grappelli/', include('grappelli.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('myprofit/', include('myprofit.urls')),

    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]


#     """ 開発環境下のみ設定 """
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
