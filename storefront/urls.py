from django.contrib import admin
from django.urls import path, include
import debug_toolbar

admin.site.site_header = 'Storefront Admin'
admin.site.index_title = 'Storefront Adminstration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('__debug__', include('debug_toolbar.urls')),
]
