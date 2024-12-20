"""
URL configuration for Facial_Recognition_Monitoring_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="index"),
    path('student_login/',views.student_login,name="student_login"),
    path('teacher_login/',views.teacher_login,name="teacher_login"),
    path('admin_login/',views.admin_login,name="admin_login"),
]
if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL,document_root=settings.STATICFILES_DIRS[0])
   urlpatterns += static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)

