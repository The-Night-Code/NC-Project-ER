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
from ERapp.views import main_Page,Home, LoginU, LogoutU , ProfileU,forgot_password ,img_upload_image,showimage,VT_Page_edit_state
from ERapp.views import download_K_file,save_signature,VT_Page,Kizeo_form_page,kizeo_form_Pieces,kizeo_form_Pieces_delete,create_acc_ai,create_acc_be,files_history
from ERapp.views import  add_files_to_MODELS,remove_file_from_MODELS,agent_immo,agent_immo_f,send_message,BE_Page_f,BE_Page,BE_audit_ALL,BE_audit_BY_A
from ERapp import views

ai="ai"
form="form"
formK="formK"
be="be"

urlpatterns = [
    
    path('', LoginU,name="not_logged_in"),
    path('', LoginU,name="main_page"),
    path('admin/', admin.site.urls),


    path('logout/', LogoutU),
    path('profile/',ProfileU ),
    path('forgot_password/',forgot_password,name="forgot_password"),
    
    path(f'{form}T/',BE_audit_ALL ,name="fT"),
    #path(f'{form}T1/',table_view_edit ,name="editFormTable"),#remove_file_from_auditV1
    #path(f'{form}T2/',remove_file_from_MODELS ,name="remove_file_from_MODEL"),
    
    path('remove_file_from_MODELS/',remove_file_from_MODELS ,name="remove_file_from_MODEL"),
    
    
    path(f'{form}T4/',add_files_to_MODELS ,name="add_files_to_model"),
    #path('formT5/',chat_box_1 , name="send_message_box1" ),
    path('send-message/',send_message , name="send_message" ),
    
    
    path('create_account_for_ai/', create_acc_ai, name="create_acc_for_AI" ),
    path('create_account_for_be/', create_acc_be, name="create_acc_for_BE" ),
    path('historique_des_fichiers/', files_history, name="files_history" ),
    
    path(f'{ai}/',agent_immo ,name="ai"),
    path(f'{ai}f/',agent_immo_f ),
    
    path(f'{be}audit/',BE_audit_BY_A ,name="be_audit"),
    path(f'{be}/',BE_Page ,name="be"),
    path(f'{be}f/',BE_Page_f ),
    
    
    path('VT/', VT_Page,name="VT"),
    path('VT1/', VT_Page_edit_state, name="VT_Page_edit_state"),
    
    path('change_profile_pic/',img_upload_image ),
    path('showimage/',showimage ),
    
    
    
    
    #path(f'{formK}/',Kizeo_form_page  ),
    path(f'{formK}/<str:client_id>',Kizeo_form_page  ,name='Kizeo_form_page'),
    path('download_K_file/<str:file_id>/', download_K_file, name='download_K_file'),
    path(f'{formK}/<str:client_id>/<str:piece_id>/',kizeo_form_Pieces  ,name='kizeo_form_Pieces'),
    path(f'{formK}2/<str:client_id>/<str:piece_id>/',kizeo_form_Pieces_delete  ,name='kizeo_form_Pieces_del'),
    path('save_signature/', save_signature, name='save_signature'),
    
] #+static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)