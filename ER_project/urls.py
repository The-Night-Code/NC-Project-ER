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
from django.urls import path,re_path
from ERapp import consumers

from django.conf import settings
from django.conf.urls.static import static
from ERapp.views import  LoginU, LogoutU , ProfileU,forgot_password ,showimage,VT_Page_edit_state
from ERapp.views import download_K_file,save_signature,VT_Page,Kizeo_form_page,kizeo_form_Pieces,kizeo_form_Pieces_delete,create_acc_ai,create_acc_be,create_acc_auditeur,corbeille,Activities
from ERapp.views import remove_file_from_MODELS,agent_immo,agent_immo_f,send_message
from ERapp.views import Auditeur_Accueil,BE_Page_f,BE_Page,BE_home_page,AI_audit_ALL,AI_audit_BY_A,BE_audit_ALL,BE_audit_BY_A
from ERapp.views import download_media_folder,table_view_2,table_view_3,CBFCS,Auditor_Task_Summary,Auditor_Task_Summary_BY_A



from ERapp.views import chatPage
from django.contrib.auth.views import LoginView, LogoutView


ai="ai"
form="form"
formK="formK"
be="be"

urlpatterns = [
    path('', chatPage, name="chat-page"),    

    # login-section
    path("auth/login/", LoginView.as_view(template_name="chat/Auditeur_main_page.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
    
    path('', LoginU, name="not_logged_in"),
    path('', LoginU, name="main_page"),
    path('admin/', admin.site.urls),


    path('logout/', LogoutU),
    path('profile/',ProfileU ),
    path('forgot_password/',forgot_password,name="forgot_password"),
    
    # Auditeur Pages
    # Auditeur Pages
    # Auditeur Pages
    path('table-view/',table_view_2 ,name="table_view_2"),
    path('Accueil/',Auditeur_Accueil ,name="Auditeur_main_page"),
    
    

    
    path('BE_audit_ALL/',BE_audit_ALL ,name="BE_audit_ALL"),
    path('BE_audit_BY_A/',BE_audit_BY_A ,name="BE_audit_BY_A"),
    path('AI_audit_ALL/',AI_audit_ALL ,name="AI_audit_ALL"),
    path('AI_audit_BY_A/',AI_audit_BY_A ,name="AI_audit_BY_A"),

    path('create_account_for_ai/', create_acc_ai, name="create_acc_for_AI" ),
    path('create_account_for_be/', create_acc_be, name="create_acc_for_BE" ),
    path('create_account_for_auditeur/', create_acc_auditeur, name="create_acc_for_Auditeur" ),
    path('corbeille/', corbeille, name="corbeille" ),
    path('Activities/', Activities, name="Activities" ),
    path('Auditor_Task_Summary/',Auditor_Task_Summary ,name="Auditor_Task_Summary"),
    path('Auditor_Task_Summary_BY_A/<str:auditeur_email>/',Auditor_Task_Summary_BY_A ,name="Auditor_Task_Summary_BY_A"),
    
    path('remove_file_from_MODELS/',remove_file_from_MODELS ,name="remove_file_from_MODELS"),
    path('send-message/',send_message , name="send_message" ),
    
    
    # Agent Immo Pages
    # Agent Immo Pages
    # Agent Immo Pages
    path(f'{ai}/',agent_immo ,name="ai"),
    path(f'{ai}f/',agent_immo_f,name="aif" ),
    
    
    # Bereau d'etude Pages
    # Bereau d'etude Pages
    # Bereau d'etude Pages
    path(f'{be}_home_page/',BE_home_page ,name="be_home_page"),
    path(f'{be}/',BE_Page ,name="be"),
    path(f'{be}f/',BE_Page_f ,name="bef"),
    path('table-view-3/',table_view_3 ,name="table_view_3"),
    path('CBFCS/',CBFCS ,name="CBFCS"),
    
    # Visiteur tech Pages
    # Visiteur tech Pages
    # Visiteur tech Pages
    path('VT/', VT_Page,name="VT"),
    path('VT1/', VT_Page_edit_state, name="VT_Page_edit_state"),
    
    
    # Kiz
    # Kiz
    # Kiz
    #path(f'{formK}1/<str:client_id>',Kizeo_form_page  ,name='Kizeo_form_page'),
    path(f'{formK}/<str:client_id>/<str:page_number>',Kizeo_form_page  ,name='Kizeo_form_page'),
    path(f'{formK}1/<str:client_id>/<str:piece_id>/',kizeo_form_Pieces  ,name='kizeo_form_Pieces'),
    path(f'{formK}2/<str:client_id>/<str:piece_id>/',kizeo_form_Pieces_delete  ,name='kizeo_form_Pieces_del'),
    path('download_K_file/<str:file_id>/', download_K_file, name='download_K_file'),
        
    path('save_signature/', save_signature, name='save_signature'),
    
    
    
    
    path('download-media/', download_media_folder, name='download_media_folder'),


    
] # + static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)