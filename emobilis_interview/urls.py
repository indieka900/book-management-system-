from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('home/', include('crud_app.urls')),
    path('api/', include('crud_app.api.urls')),
    
    # vOQx4w9PMNbSAK3O
    # book-project
    # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRhendpbGlhZHVneWdpb3ljY2tmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjg3MzQxMzYsImV4cCI6MjA0NDMxMDEzNn0.qB91CZ_rLeBTXrEOHtdrrjUpRKFNv_DSfA05OwkZEtk
    # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRhendpbGlhZHVneWdpb3ljY2tmIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyODczNDEzNiwiZXhwIjoyMDQ0MzEwMTM2fQ.T1FBtBdMRClgoJgUbvv4iMX0_iWSLTUB_BnfZrpkf78
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
