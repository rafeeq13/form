"""
URL configuration for form project.

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from enroll import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('base/',views.base,name='base'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.user_logout,name='logout'),
    path('apply/',views.apply,name='apply'),
    path('addjob/',views.addjob,name='addjob'),
    path('carear/',views.openings,name='carear'),
    path('applications/',views.applications,name='applications'),
    path('edit/<int:id>/',views.editjob,name='edit'),
    path('delete/<int:id>/',views.deletejob,name='delete'),
    
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
