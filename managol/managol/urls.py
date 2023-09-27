from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views, Hod_Views, Staff_Views, Student_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base, name='base'),


    # Login Path
    path('login/', views.login, name='login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
