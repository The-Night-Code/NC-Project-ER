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
from ERapp.views import Home, LoginU, LogoutU ,table_view, ProfileU ,img_upload_image,showimage
from ERapp.views import table_view_edit ,add_files_to_MODELS,remove_file_from_MODELS,agent_immo,agent_immo_f,chat_box_1,Kizeo_form_page
from ERapp import views

ai="ai"
form="form"
formK="formK"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home),
    path('login/', LoginU),
    path('logout/', LogoutU),
    path('profile/',ProfileU ),
    path(f'{form}T/',table_view ),
    path(f'{form}T1/',table_view_edit ,name="editFormTable"),#remove_file_from_auditV1
    path(f'{form}T2/',remove_file_from_MODELS ,name="remove_file_from_MODEL"),
    path(f'{form}T4/',add_files_to_MODELS ,name="add_files_to_model"),
    
    path(f'{ai}/',agent_immo ),
    path(f'{ai}f/',agent_immo_f ),
    
    path('change_profile_pic/',img_upload_image ),
    path('showimage/',showimage ),
    
    path('formT5/',chat_box_1 , name="send_message_box1" ),
    
    
    path(f'{formK}/',Kizeo_form_page  ),
   
    
    
] #+static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)