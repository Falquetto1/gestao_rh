from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.website.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('empresas/', include('apps.empresas.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
]
