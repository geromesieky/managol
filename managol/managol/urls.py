from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views, Administration_Views, Staff_Views, Student_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base, name='base'),

    # Login Path
    path('', views.user_login, name='login'),
    path('do-login', views.do_login, name='do_login'),
    path('do-logout', views.do_logout, name='do_logout'),

    # Update Profile
    path('profile', views.profile, name='profile'),
    path('profile/update', views.profile_update, name='profile_update'),

    # This Hod panel Url
    path('administration/home', Administration_Views.home, name='administration_home'),
    path('administration/student/add', Administration_Views.add_student, name='add_student'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
