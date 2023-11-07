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
from ERapp.views import main_Page,Home, LoginU, LogoutU , ProfileU,forgot_password ,showimage,VT_Page_edit_state
from ERapp.views import download_K_file,save_signature,VT_Page,Kizeo_form_page,kizeo_form_Pieces,kizeo_form_Pieces_delete,create_acc_ai,create_acc_be,files_history,Activities
from ERapp.views import remove_file_from_MODELS,agent_immo,agent_immo_f,send_message
from ERapp.views import Auditeur_Accueil,BE_Page_f,BE_Page,AI_audit_ALL,AI_audit_BY_A,BE_audit_ALL,BE_audit_BY_A
from ERapp import views

ai="ai"
form="form"
formK="formK"
be="be"

urlpatterns = [
    
    path('', LoginU, name="not_logged_in"),
    path('', LoginU, name="main_page"),
    path('admin/', admin.site.urls),


    path('logout/', LogoutU),
    path('profile/',ProfileU ),
    path('forgot_password/',forgot_password,name="forgot_password"),
    
    path('Accueil/',Auditeur_Accueil ,name="Auditeur_main_page"),
    path('BE_audit_ALL/',BE_audit_ALL ,name="BE_audit_ALL"),
    path('BE_audit_BY_A/',BE_audit_BY_A ,name="BE_audit_BY_A"),
    path('AI_audit_ALL/',AI_audit_ALL ,name="AI_audit_ALL"),
    path('AI_audit_BY_A/',AI_audit_BY_A ,name="AI_audit_BY_A"),

    path('remove_file_from_MODELS/',remove_file_from_MODELS ,name="remove_file_from_MODEL"),

    path('send-message/',send_message , name="send_message" ),
    
    
    path('create_account_for_ai/', create_acc_ai, name="create_acc_for_AI" ),
    path('create_account_for_be/', create_acc_be, name="create_acc_for_BE" ),
    path('historique_des_fichiers/', files_history, name="files_history" ),
    path('Activities/', Activities, name="Activities" ),
    
    path(f'{ai}/',agent_immo ,name="ai"),
    path(f'{ai}f/',agent_immo_f ),
    
    
    path(f'{be}/',BE_Page ,name="be"),
    path(f'{be}f/',BE_Page_f ),
    
    
    path('VT/', VT_Page,name="VT"),
    path('VT1/', VT_Page_edit_state, name="VT_Page_edit_state"),
    
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