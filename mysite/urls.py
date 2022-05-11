from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from filebrowser.sites import site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('summernote/', include('django_summernote.urls')),

    path('myinfo/', include('myinfo.urls')),
    path('', RedirectView.as_view(url='/myinfo/')),

    path('mysched/', include('mysched.urls')),
    # path('mycontact/', include('mycontact.urls')),
    path('sample/', include('sample.urls')),
    path('myreport/', include('myreport.urls')),

    # path('admin/filebrowser/', site.urls),
    # path('grappelli/', include('grappelli.urls')),
    path('tinymce/', include('tinymce.urls')),
]


#     """ 開発環境下のみ設定 """
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
