from django.contrib import admin
from django.urls import path, include
from block.views import Register
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('block.urls')),
    path('register/', Register.as_view(), name='singup')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
