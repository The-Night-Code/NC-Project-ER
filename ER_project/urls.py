"""
URL configuration for ER_project project.

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
from ERapp.views import Home, LoginU, LogoutU ,table_view, ProfileU ,img_upload_image,showimage,table_view_edit  ,add_files_to_MODELS,remove_file_from_MODELS
from ERapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home),
    path('login/', LoginU),
    path('logout/', LogoutU),
    path('profile/',ProfileU ),
    path('formT/',table_view ),
    path('formT1/',table_view_edit ,name="editFormTable"),#remove_file_from_auditV1
    path('formT2/',remove_file_from_MODELS ,name="remove_file_from_MODEL"),
    path('formT4/',add_files_to_MODELS ,name="add_files_to_model"),
    
    
    
    path('change_profile_pic/',img_upload_image ),
    path('showimage/',showimage ),
    
    
    
   
    
    
] #+static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)