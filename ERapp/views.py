from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.models import User

from django.shortcuts import redirect , get_object_or_404
from django.contrib.auth import authenticate, login , logout

from django.views.generic.edit import CreateView



from .models import ImageModel,USER,TableData001,kizeo_model,message_box_1
from .models import file_table_auditV1,file_table_auditV2,file_table_auditV3,file_table_vt,file_table_auditFinal

from django.core.mail import send_mail
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Create your views here.
import random
import string


import openpyxl
from openpyxl.utils import get_column_letter
from openpyxl.drawing.image import Image
from django.http import HttpResponse
from .models import MyModel, UpdatedXLSXFile 
from openpyxl.styles import NamedStyle


formT="/formT/"
link2="/agentimmo/"

def Home(request):

    
    #return render(request,'html/home.html',{"name":"night","username":"nightcode"})
    return render(request,'html/home.html')
    
def send_email():
    send_mail(
    "Subject here",
    "Here is the message. test test 123 ",
    "guhgi155@gmail.com",
    ["lazariatik@gmail.com"],
    fail_silently=False,) 



def LoginU(request):
    
    
    if request.method == "POST":
        
        usernameU =request.POST.get('username')
        passwordU =request.POST.get('password')
        
        user = authenticate(username=usernameU,password=passwordU)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(formT) 

    #if loginU:
     #   if emailU=="night" :
      #      return HttpResponseRedirect('/home')  
    
    return render(request,'html/login.html')




def SignupU(request):
    
    
    pl=False
    pm=False
    pc=False
    pn=False
    per=False
    if request.method == 'POST':
        username =request.POST.get('username')
        emailU =request.POST.get('email')
        pw1 =request.POST.get('password1')
        pw2 =request.POST.get('password2')
        
        per = True
        
        
        if str(pw1) == str(pw2):
            pm=True
            for i in str(pw1):
                # if string has letter
                if i in "abcdefghijklmnopqrstuvwxyz" or i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    pc = True
                # if string has number
                if i in "0123456789":
                    pn = True

        
        if len(str(pw1)) >= 8 :
            pl=True
            
    
        if pl and pm and pc and pn :
            data = User.objects.create_user(username=username, email=emailU , password=pw1)
            data.save()
            return render(request, 'html/home.html')

        
    return render(request, 'html/signup.html',{"per":per,"pl":pl,"pm":pm,"pc":pc,"pn":pn})
    
    
    
    
def LogoutU(request):
    logout(request)
    return redirect("/login/")
    #return render(request,'html/login.html')
    
    
def ProfileU(request):
    #user_Id="3"
    user_L=USER.objects.get(email="night@gmail.com") 
    
    Submit_Upload_image=request.POST.get("Submit_Upload_image")
    remove_profile_image=request.POST.get("remove_profile_image")
    
    # Upload Profile Image
    if request.method == 'POST' :
        user_L = USER.objects.get(email="night@gmail.com")
        if Submit_Upload_image=="Submit_Upload_image" and request.FILES['my_uploaded_image']:
            imagefile = request.FILES['my_uploaded_image']
            user_L.profile_pic =imagefile 
            user_L.save(update_fields=['profile_pic'])
            
        if remove_profile_image=="remove_profile_image":
            
            user_L.profile_pic =None 
            user_L.save(update_fields=['profile_pic'])
            
        return redirect("/profile/")
        
    
    
    profile_image =user_L.profile_pic
    if profile_image :
        #profile_image="{% static 'image/default_user_avatar.png' %}"
        profile_image =user_L.profile_pic.url
    

    return render(request,'html/profileU.html',{'profile_image':profile_image})

def showimage(request):
    profile_img = ImageModel.objects.get(user_id="n123") 
    return render(request,'html/showimage.html',{'profile_image': profile_img})


    
    
def img_upload_image(request):
    
    return redirect('/profileU/')
    
    
    
    

    

def generate_random_string(length):
    characters = string.ascii_letters + string.digits  # You can customize this for your needs
    random_string = ''.join(random.choice(characters) for _ in range(length))
    random_string=random_string.replace("%20","")
    random_string=random_string.replace(" ","")
    return random_string
    
def table_view(request): # add row
    
    
    if request.method == 'POST' :
        
        myID1=request.POST.get("myid1")
        column1=request.POST.get("col_type1")
        
        l1="table1_input_files_to_"+str(myID1)
        #return redirect(f"/{myID}_{column}/")
        if request.POST.get("mybutton1") == 'clicked':
            inp_files=request.FILES.getlist(l1)  
            #inp_files=request.FILES["table1_input_files_to_"+str(myID)]
            file_table = ModelByColumn(column1)

            for file in request.FILES.getlist(l1):
                format_file=file.name.split(".")[1]
                if format_file in ['jpg','png','jpeg','heic']:
                    format_file="image"
                if format_file in ['doc','docx']:
                    format_file="word"
                    
                if format_file in ['xls','xlsm']:
                    format_file="excel"  
                
                file_table.objects.create(
                    file_id = myID1,
                    file_name = file.name,
                    file_save = file,
                    file_format =format_file
                
                )
        
        
        myID2=request.POST.get("myid2")
        column2=request.POST.get("col_type2")
        
        l2="table2_input_files_to_"+str(myID2)
        #return redirect(f"/{myID}_{column}/")
        if request.POST.get("mybutton2") == 'clicked':
            inp_files=request.FILES.getlist(l2)  
            #inp_files=request.FILES["table1_input_files_to_"+str(myID)]
            file_table = ModelByColumn(column2)

            for file in request.FILES.getlist(l2):
                format_file=file.name.split(".")[1]
                if format_file in ['jpg','png','jpeg','heic']:
                    format_file="image"
                if format_file in ['doc','docx']:
                    format_file="word"
                    
                if format_file in ['xls','xlsm']:
                    format_file="excel"  
                
                file_table.objects.create(
                    file_id = myID2,
                    file_name = file.name,
                    file_save = file,
                    file_format =format_file
                
                )
      
        myID3=request.POST.get("myid3")
        column3=request.POST.get("col_type3")
        l3="table3_input_files_to_"+str(myID3)
        
        if request.POST.get("mybutton3") == 'clicked':
            inp_files=request.FILES.getlist(l3)  
            #inp_files=request.FILES["table1_input_files_to_"+str(myID)]
            file_table = ModelByColumn(column3)

            for file in request.FILES.getlist(l3):
                format_file=file.name.split(".")[1]
                if format_file in ['jpg','png','jpeg','heic']:
                    format_file="image"
                if format_file in ['doc','docx']:
                    format_file="word"
                    
                if format_file in ['xls','xlsm']:
                    format_file="excel"  
                
                file_table.objects.create(
                    file_id = myID3,
                    file_name = file.name,
                    file_save = file,
                    file_format =format_file
                
                )
                
        
        return redirect(formT)
    
    

    data = TableData001.objects.all()
    
    col_count = data.count()
    # Get unique column names from the TableData model
    column_names = TableData001._meta.get_fields()
    datafiles_VT = file_table_vt.objects.all()
    datafiles_AuditV1 = file_table_auditV1.objects.all()
    datafiles_AuditV2 = file_table_auditV2.objects.all()
    datafiles_AuditV3 = file_table_auditV3.objects.all()
    datafiles_AuditFinal = file_table_auditFinal.objects.all()
    message_box_01 = message_box_1.objects.all()
    return render(request, 'html/formPage.html', { 'data': data ,
                                                  'col_count':col_count ,
                                                  'column_names': column_names,
                                                  'datafiles_VT': datafiles_VT ,
                                                  'datafiles_AuditV1': datafiles_AuditV1 ,
                                                  'datafiles_AuditV2': datafiles_AuditV2 ,
                                                  'datafiles_AuditV3': datafiles_AuditV3 ,
                                                  'datafiles_AuditFinal':datafiles_AuditFinal,
                                                  'message_box_1':message_box_01})
       
    
    

    
def table_view_edit(request):
    param_value_id = request.GET.get('param0')
    param1_value = request.GET.get('param1')
    param2_value = request.GET.get('param2')
    param3_value = request.GET.get('param3')
    param4_value = request.GET.get('param4')
    #param5_value = request.FILES.getlist('param5')
    param6_value = request.GET.get('param6')
    param7_value = request.GET.get('param7')
    #if param2_value or param3_value:
    try:
        get_col_by_id = TableData001.objects.get(cell_id=str(param_value_id))
    except TableData001.DoesNotExist:
        pass
     
    if get_col_by_id:
        get_col_by_id.firstname =  param1_value 
        get_col_by_id.lastname = param2_value
        get_col_by_id.address = param3_value
        get_col_by_id.num = param4_value
       
        get_col_by_id.etat = param6_value 
        get_col_by_id.paiement = param7_value
        #get_col_by_id.save(update_fields=['firstname', 'lastname','address','num','vt','etat'])
        get_col_by_id.save(update_fields=['firstname', 'lastname','address','num','etat','paiement'])
    return redirect(formT)

       
    

def ModelByColumn(model_by_column):
    if model_by_column == "vt":
        return file_table_vt
    if model_by_column == "auditV1":
        return file_table_auditV1
    if model_by_column == "auditV2":
        return file_table_auditV2
    if model_by_column == "auditV3":
        return file_table_auditV3
    if model_by_column == "auditFinal":
        return file_table_auditFinal
    
def remove_file_from_MODELS(request):
    file_id = request.GET.get('param0')
    index = request.GET.get('param1')
    model_by_column = request.GET.get('param2')
    file_table=ModelByColumn(model_by_column)
    

    try:
        f_table_audit_v1 =file_table.objects.get(file_id=str(file_id),file_index=str(index))
    except file_table.DoesNotExist:
        pass
    
    f_table_audit_v1.delete()
    return redirect(formT)


def add_files_to_MODELS(request):
    
    return redirect("/tt/")
    file_id = request.POST.get('file_id') 
    column = request.POST.get('column')
    files = request.FILES.getlist('fileInput') #table1_input_files_to_
   
    
    add_files_to_model =file_table_auditV1()

    if str(column)=="auditV1":
        try:
            add_files_to_model =file_table_auditV1()
        except add_files_to_model.DoesNotExist:
            pass
    elif str(column)=="auditV2":
        try:
            add_files_to_model =file_table_auditV2()
        except add_files_to_model.DoesNotExist:
            pass
    elif str(column)=="auditV3":
        try:
            add_files_to_model =file_table_auditV3()
        except add_files_to_model.DoesNotExist:
            pass
    elif str(column)=="vt":
        try:
            add_files_to_model =file_table_vt()
        except add_files_to_model.DoesNotExist:
            pass
    
    
    
    #if files:
    for file in files:
        file_table_auditV1.objects.create(
            file_id = file_id,
            file_name = file.name.split("/")[1],
            file_save = file,
            file_format =file.name.split(".")[1]
            
        )
            
    
    return redirect(formT)


def agent_immo(request):

    data = TableData001.objects.all()
    
    col_count = data.count()
    # Get unique column names from the TableData model
    column_names = TableData001._meta.get_fields()
    datafiles_VT = file_table_vt.objects.all()
    datafiles_AuditV1 = file_table_auditV1.objects.all()
    datafiles_AuditV2 = file_table_auditV2.objects.all()
    datafiles_AuditV3 = file_table_auditV3.objects.all()
    datafiles_AuditFinal = file_table_auditFinal.objects.all()
    return render(request, 'html/agentimmo.html', { 'data': data ,
                                                  'col_count':col_count ,
                                                  'column_names': column_names,
                                                  'datafiles_VT': datafiles_VT ,
                                                  'datafiles_AuditFinal':datafiles_AuditFinal})

def agent_immo_f(request):
    

    return render(request, 'html/agentimmof.html', )


def chat_box_1(request):
    cell_id = request.GET.get('param0')
    
    user_email = request.GET.get('param1')
    user_firstname = request.GET.get('param2')
    user_lastname = request.GET.get('param3')
    box = request.GET.get('param4')
    msg = request.GET.get('param5')
    
    msg_id =generate_random_string(8)
    

    
    message_box_1.objects.create(
                message_id = msg_id,
                row_id = cell_id,
                username =user_firstname + " , " +  user_lastname,
                email =  user_email,
                message =msg,
                box =box
            )
    
        
    return redirect(formT)




def update_xlsx_template(request):
    # Load your XLSX template
    
    template_path = 'ERapp\static\Kizeo.xlsx'  # Provide the path to your template file
    workbook = openpyxl.load_workbook(template_path)
    
    ws1 = workbook["Données"]
    worksheet3 =  workbook["Garde"]
    worksheet4 =  workbook["Site"]
    #for i in range(2,17):
        #ws1[f"B{i}"].value ="night code"
    
    ws1["B2"].value ="night code"
    ws1["B4"].value ="derb seltan"
    
    
    ############################# WORK SHEET 2
    ############################# WORK SHEET 2
    ############################# WORK SHEET 2
    ############################# WORK SHEET 2
    ############################# WORK SHEET 2
    worksheet = workbook["Métré"]  # Select the first sheet or specify the sheet name
    # Fetch data from your Django model (Assuming you have a queryset)
    obj = MyModel.objects.get(text_field="t1")

    


    
    for i in range(3,17):
        
        # Find and update text cells
        text_cell = worksheet[f'f{i}']  # Example: Replace 'A1' with the actual cell containing text
        text_cell.value = "non" #obj.text_field

        for c_name in ["A","B","C"]:
            # Find and update image cells (assuming image_field is a Django ImageField)
            image_cell = worksheet[f'{c_name}{i}']  # Example: Replace 'B1' with the actual cell containing the image
            image_cell.value = None
            #image_cell.hyperlink = None
            image_list = [obj.image_field.path,obj.image_field_2.path,obj.image_field_3.path]
            image_path = random.choice(image_list)
            
            
            # Load the image
            img = Image(image_path)

            # Calculate the image size to fit the cell
            cell_width = worksheet.column_dimensions[get_column_letter(image_cell.column)].width
            cell_height = worksheet.row_dimensions[image_cell.row].height
            img.width =  199.68 #cell_width
            img.height = 149.76# cell_height
            
            worksheet.column_dimensions[c_name].width = 29.86
            #worksheet.row_dimensions['4'].height = 127
            
            # Add the new image to the cell
            worksheet.add_image(img, image_cell.coordinate)
        
    ############################# END WORK SHEET 2
    ############################# END WORK SHEET 2
    ############################# END WORK SHEET 2
    ############################# END WORK SHEET 2

    
    
    ############################################### sheet 3 image
    image_cell2 = worksheet3['B6']  # Example: Replace 'B1' with the actual cell containing the image
    image_cell2.value = None
    #image_cell2.hyperlink = None
    image_path2 = obj.image_field.path

    # Load the image
    img2 = Image(image_path2)

    # Calculate the image size to fit the cell
    img2.width =  371.52 #cell_width
    img2.height = 280.32# cell_height
    #worksheet3.column_dimensions['B6'].width = 29.86
    #worksheet.row_dimensions['4'].height = 127
    # Add the new image to the cell
    worksheet3.add_image(img2, image_cell2.coordinate)
    
    
    
    
    ############################## header
    ############################## header
    ############################## header
    # Load the image
    img3 = Image(image_path2)
    # Calculate the image size to fit the cell
    img3.width =  50 #cell_width
    img3.height = 30# cell_height
    worksheet3.oddHeader.center.text = "&L &G &C Your Image Placeholder &R"
    ############################## header
    ############################## header
    ############################## header
        
    
    
    
    ######################################   WORK_SHEET_4
    ######################################   WORK_SHEET_4
    ######################################   WORK_SHEET_4
    # A38 E38 
    # A50 E50
    # B67
    
    image_cell_1 = worksheet4['A38']  # Example: Replace 'B1' with the actual cell containing the image
    image_cell_1.value = None
    #image_cell_1.hyperlink = None
    image_path1 = obj.image_field_2.path
    img_1 = Image(image_path1)
    img_1.width =  185.28 #cell_width
    img_1.height = 140.16 # cell_height
    worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    
    image_cell_1 = worksheet4['E38']  # Example: Replace 'B1' with the actual cell containing the image
    image_cell_1.value = None
    #image_cell_1.hyperlink = None
    # image url
    image_path1 = obj.image_field_3.path
    img_1 = Image(image_path1)
    img_1.width =  185.28 #cell_width
    img_1.height = 140.16 # cell_height
    worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    
    image_cell_1 = worksheet4['E50']  # Example: Replace 'B1' with the actual cell containing the image
    image_cell_1.value = None
    #image_cell_1.hyperlink = None
    image_path1 = obj.image_field_2.path
    img_1 = Image(image_path1)
    img_1.width =  185.28 #cell_width
    img_1.height = 140.16 # cell_height
    worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    
    image_cell_1 = worksheet4['A50']  # Example: Replace 'B1' with the actual cell containing the image
    image_cell_1.value = None
    #image_cell_1.hyperlink = None
    # image url
    image_path1 = obj.image_field_3.path
    img_1 = Image(image_path1)
    img_1.width =  185.28 #cell_width
    img_1.height = 140.16 # cell_height
    worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    
    image_cell_1 = worksheet4['B67']  # Example: Replace 'B1' with the actual cell containing the image
    image_cell_1.value = None
    #image_cell_1.hyperlink = None
    # image url
    image_path1 = obj.image_field_3.path
    img_1 = Image(image_path1)
    img_1.width =  185.28 #cell_width
    img_1.height = 140.16 # cell_height
    worksheet4.add_image(img_1, image_cell_1.coordinate)
    ######################################   END WORK_SHEET_4
    ######################################   END WORK_SHEET_4
    ######################################   END WORK_SHEET_4
    
    


    ###################################################### save process #######################################################
    # Save the updated XLSX file temporarily
    temp_xlsx_path = 'path_to_temp_xlsx.xlsx'  # Provide a temporary path on your server
    workbook.save(temp_xlsx_path)

    # Create a new instance of your other model
    updated_xlsx = UpdatedXLSXFile()

    # Assign the XLSX file to the FileField or ImageField of the new model instance
    updated_xlsx.xlsx_file.save('updated_template.xlsx', open(temp_xlsx_path, 'rb'))

    # Save the new model instance to persist the XLSX file
    updated_xlsx.save()

    return HttpResponse('XLSX file updated and saved to another model.')



def Kizeo_form_page(request,client_id):

    if kizeo_model.objects.filter(kizeo_id=client_id):
            pass
    else:
        kizeo_model.objects.create(kizeo_id=client_id)
    
    obj = kizeo_model.objects.get(kizeo_id=client_id)
    if request.method == 'POST':
        
            
       
        
        submit_to_Kizeo = request.POST.get("submit_to_Kizeo")
        if submit_to_Kizeo=="submit":
            
            ### Façades
            Facade_1_Orientation = request.POST.get("Facade_1_Orientation")
            Facade_1_Mitoyennete = request.POST.get("Facade_1_Mitoyennete")
            Facade_1_Longueur = float(request.POST.get("Facade_1_Longueur"))
            Facade_1_Hauteur = float(request.POST.get("Facade_1_Hauteur"))
            #Facade_1_Surfac = request.POST.get("Facade_1_Surfac")
            #Facade_1_Photo_Principale = request.FILES['Facade_1_Photo_Principale']
            
            Facade_2_Orientation = request.POST.get("Facade_2_Orientation")
            Facade_2_Mitoyennete = request.POST.get("Facade_2_Mitoyennete")
            Facade_2_Longueur = float(request.POST.get("Facade_2_Longueur"))
            Facade_2_Hauteur = float(request.POST.get("Facade_2_Hauteur"))
            #Facade_2_Surfac = request.POST.get("Facade_2_Surfac")
            #Facade_2_Photo_Principale = request.FILES['Facade_2_Photo_Principale']
            
            Facade_3_Orientation = request.POST.get("Facade_3_Orientation")
            Facade_3_Mitoyennete = request.POST.get("Facade_3_Mitoyennete")
            Facade_3_Longueur = float(request.POST.get("Facade_3_Longueur"))
            Facade_3_Hauteur = float(request.POST.get("Facade_3_Hauteur"))
            #Facade_3_Surfac = request.POST.get("Facade_3_Surfac")
            #Facade_3_Photo_Principale = request.FILES['Facade_3_Photo_Principale']
            
            Facade_4_Orientation = request.POST.get("Facade_4_Orientation")
            Facade_4_Mitoyennete = request.POST.get("Facade_4_Mitoyennete")
            Facade_4_Longueur = float(request.POST.get("Facade_4_Longueur"))
            Facade_4_Hauteur = float(request.POST.get("Facade_4_Hauteur"))
            #Facade_4_Surfac = request.POST.get("Facade_4_Surfac")
            #Facade_4_Photo_Principale = request.FILES['Facade_4_Photo_Principale']
            
            
            ### Cauffage
            Cauffage_systeme = request.POST.get("Cauffage_systeme")
            Cauffage_annee_de_mise_en_oeuvre = int(request.POST.get("Cauffage_annee_de_mise_en_oeuvre"))
            #Cauffage_photo_systeme_de_production = request.FILES['Cauffage_photo_systeme_de_production']
            #Cauffage_photo_fiche_signaletique = request.FILES['Cauffage_photo_fiche_signaletique']
            Cauffage_type_de_regulation = request.POST.get("Cauffage_type_de_regulation")
            Cauffage_system_d_appoint = request.POST.get("Cauffage_system_d_appoint")
            #Cauffage_photo_appoint = request.FILES['Cauffage_photo_appoint']
            Cauffage_commentaire = request.POST.get("Cauffage_commentaire")
                
            ### ECS
            ECS_type =request.POST.get("ECS_type")
            ECS_system_d_appoint = request.POST.get("ECS_system_d_appoint")
            #ECS_photo_appoint = request.FILES['ECS_photo_appoint']
            ECS_commentaire = request.POST.get("ECS_commentaire")

            ### Ventilation
            Ventilation_type = request.POST.get("ECS_type")
            #Ventilation_photo_ventilation = request.FILES['Ventilation_photo_ventilation']
            
            ### Refroidissement
            Refroidissement_type = request.POST.get("Refroidissement_type")
            Refroidissement_commentaire = request.POST.get("Refroidissement_commentaire")
            
            ### Compteur Electrique
            Compteur_Electrique_Puissance_souscrite = request.POST.get("Compteur_Electrique_Puissance_souscrite")
            Compteur_Electrique_type = request.POST.get("Compteur_Electrique_type")
            #Compteur_Electrique_photo_compteur = request.FILES['Compteur_Electrique_photo_compteur']
            Compteur_Electrique_commentaire = request.POST.get("Compteur_Electrique_commentaire")
            
            ### Mur 1
            obj.Mur_1_Position = request.POST.get("Mur_1_Position")
            obj.Mur_1_Composition = request.POST.get("Mur_1_Composition")
            obj.Mur_1_Epaisseur_mur = request.POST.get("Mur_1_Epaisseur_mur")
            obj.Mur_1_Isolation = request.POST.get("Mur_1_Isolation")
            obj.Mur_1_Epaisseur_isolant = request.POST.get("Mur_1_Epaisseur_isolant")
            obj.Mur_1_Date_d_isolation = request.POST.get("Mur_1_Date_d_isolation")
            obj.Mur_1_Preuve_d_isolation = request.POST.get("Mur_1_Preuve_d_isolation")
            #obj.Mur_1_Photo_mur = request.FILES['Mur_1_Photo_mur']
            
            
            
            obj.Facade_1_Orientation = Facade_1_Orientation
            obj.Facade_1_Mitoyennete = Facade_1_Mitoyennete
            obj.Facade_1_Longueur = Facade_1_Longueur
            obj.Facade_1_Hauteur =  Facade_1_Hauteur
            obj.Facade_1_Surface =Facade_1_Longueur * Facade_1_Hauteur 
            #obj.Facade_1_Photo_Principale =Facade_1_Photo_Principale
            
            obj.Facade_2_Orientation = Facade_2_Orientation
            obj.Facade_2_Mitoyennete = Facade_2_Mitoyennete
            obj.Facade_2_Longueur = Facade_2_Longueur
            obj.Facade_2_Hauteur =  Facade_2_Hauteur
            obj.Facade_2_Surface =Facade_2_Longueur * Facade_2_Hauteur 
            #obj.Facade_2_Photo_Principale =Facade_2_Photo_Principale
            
            obj.Facade_3_Orientation = Facade_3_Orientation
            obj.Facade_3_Mitoyennete = Facade_3_Mitoyennete
            obj.Facade_3_Longueur = Facade_3_Longueur
            obj.Facade_3_Hauteur =  Facade_3_Hauteur
            obj.Facade_3_Surface =Facade_3_Longueur * Facade_3_Hauteur 
            #obj.Facade_3_Photo_Principale =Facade_3_Photo_Principale
            
            obj.Facade_4_Orientation = Facade_4_Orientation
            obj.Facade_4_Mitoyennete = Facade_4_Mitoyennete
            obj.Facade_4_Longueur = Facade_4_Longueur
            obj.Facade_4_Hauteur =  Facade_4_Hauteur
            obj.Facade_4_Surface =Facade_4_Longueur * Facade_4_Hauteur 
            #obj.Facade_4_Photo_Principale =Facade_4_Photo_Principale
            
            ### Cauffage
            obj.Cauffage_systeme = Cauffage_systeme
            obj.Cauffage_annee_de_mise_en_oeuvre = Cauffage_annee_de_mise_en_oeuvre
            #obj.Cauffage_photo_systeme_de_production = Cauffage_photo_systeme_de_production
            #obj.Cauffage_photo_fiche_signaletique = Cauffage_photo_fiche_signaletique
            obj.Cauffage_type_de_regulation = Cauffage_type_de_regulation
            obj.Cauffage_system_d_appoint = Cauffage_system_d_appoint
            #obj.Cauffage_photo_appoint = Cauffage_photo_appoint
            obj.Cauffage_commentaire =Cauffage_commentaire
            
            ### ECS
            obj.ECS_type = ECS_type
            obj.ECS_system_d_appoint = ECS_system_d_appoint
            #obj.ECS_photo_appoint = ECS_photo_appoint
            obj.ECS_commentaire = ECS_commentaire
            
            ### Ventilation
            obj.Ventilation_type = Ventilation_type
            #obj.Ventilation_photo_ventilation = Ventilation_photo_ventilation
            
            ### Refroidissement
            obj.Refroidissement_type = Refroidissement_type
            obj.Refroidissement_commentaire = Refroidissement_commentaire
            
            ### Compteur Electrique
            obj.Compteur_Electrique_Puissance_souscrite = Compteur_Electrique_Puissance_souscrite
            obj.Compteur_Electrique_type = Compteur_Electrique_type
            #obj.Compteur_Electrique_photo_compteur = Compteur_Electrique_photo_compteur
            obj.Compteur_Electrique_commentaire = Compteur_Electrique_commentaire
            
            ### Mur 1
            #obj.Mur_1_Position = Mur_1_Position
            #obj.Mur_1_Composition = Mur_1_Composition
            #obj.Mur_1_Epaisseur_mur = Mur_1_Epaisseur_mur
            #obj.Mur_1_Isolation = Mur_1_Isolation
            #obj.Mur_1_Epaisseur_isolant = Mur_1_Epaisseur_isolant
            #obj.Mur_1_Date_d_isolation = Mur_1_Date_d_isolation
            #obj.Mur_1_Preuve_d_isolation = Mur_1_Preuve_d_isolation
            #obj.Mur_1_Photo_mur = Mur_1_Photo_mur
            
            obj.save(update_fields=['Facade_1_Orientation', 'Facade_1_Mitoyennete','Facade_1_Longueur','Facade_1_Hauteur','Facade_1_Surface',#'Facade_1_Photo_Principale',
                                    'Facade_2_Orientation', 'Facade_2_Mitoyennete','Facade_2_Longueur','Facade_2_Hauteur','Facade_2_Surface',#'Facade_2_Photo_Principale',
                                    'Facade_3_Orientation', 'Facade_3_Mitoyennete','Facade_3_Longueur','Facade_3_Hauteur','Facade_3_Surface',#'Facade_3_Photo_Principale',
                                    'Facade_4_Orientation', 'Facade_4_Mitoyennete','Facade_4_Longueur','Facade_4_Hauteur','Facade_4_Surface',#'Facade_4_Photo_Principale',
                                     
                                    ### Cauffage
                                    "Cauffage_systeme",
                                    "Cauffage_annee_de_mise_en_oeuvre",
                                    #"Cauffage_photo_systeme_de_production",
                                    #"Cauffage_photo_fiche_signaletique",
                                    "Cauffage_type_de_regulation",
                                    "Cauffage_system_d_appoint",
                                    #"Cauffage_photo_appoint" ,
                                    "Cauffage_commentaire" ,
                                    
                                    ### ECS
                                    "ECS_type",
                                    "ECS_system_d_appoint",
                                    #"ECS_photo_appoint" ,
                                    "ECS_commentaire",
                                    
                                    ### Ventilation
                                    "Ventilation_type" ,
                                    #"Ventilation_photo_ventilation" ,
                                    
                                    ### Refroidissement
                                    "Refroidissement_type" ,
                                    "Refroidissement_commentaire" ,
                                    
                                    ### Compteur Electrique
                                    "Compteur_Electrique_Puissance_souscrite" ,
                                    "Compteur_Electrique_type" ,
                                    #"Compteur_Electrique_photo_compteur" ,
                                    "Compteur_Electrique_commentaire" ,
                                    
                                    ### Mur 1
                                    "Mur_1_Position", 
                                    "Mur_1_Composition",
                                    "Mur_1_Epaisseur_mur",
                                    "Mur_1_Isolation",
                                    "Mur_1_Epaisseur_isolant",
                                    "Mur_1_Date_d_isolation",
                                    "Mur_1_Preuve_d_isolation",
                                    #"Mur_1_Photo_mur",
                                    
                                ])

                
                
     
            
            
        
            ######################################   WORK_SHEET_4
            ######################################   WORK_SHEET_4
            ######################################   WORK_SHEET_4

            
    
    
    data = kizeo_model.objects.get(kizeo_id=client_id)
    return render(request, 'html/formK.html',{"data":data})



def download_K_file(request,file_id):
    obj = kizeo_model.objects.get(kizeo_id=file_id)
    template_path = 'ERapp\static\Kizeo.xlsx'  # Provide the path to your template file
    workbook = openpyxl.load_workbook(template_path)
    
    worksheet1 = workbook["Données"]
    worksheet2 = workbook["Métré"]
    worksheet3 = workbook["Garde"]
    worksheet4 = workbook["Site"]
    ################################### start Facade
    text_cell = worksheet4['A33']  
    text_cell.value = obj.Facade_1_Orientation
    text_cell = worksheet4['A34']  
    text_cell.value = obj.Facade_1_Mitoyennete
    text_cell = worksheet4['A35'] 
    text_cell.value = f"Longueur = {obj.Facade_1_Longueur}"
    text_cell = worksheet4['A36']  
    text_cell.value = f"Hauteur = {obj.Facade_1_Hauteur}"
    text_cell = worksheet4['A37']  
    text_cell.value = f"Surface = {obj.Facade_1_Surface}"
    
    image_cell_1 = worksheet4['A38'] 
    image_cell_1.value = None
    #image_cell_1.hyperlink = None
    if obj.Facade_1_Photo_Principale:
        image_path_ = obj.Facade_1_Photo_Principale.path  # Get the file path
        if default_storage.exists(image_path_):
            image_path1 = obj.Facade_1_Photo_Principale.path
            img_1 = Image(image_path1)
            img_1.width =  185.28 #cell_width
            img_1.height = 140.16 # cell_height
            worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    
    
    text_cell = worksheet4['E33']  
    text_cell.value = obj.Facade_2_Orientation
    text_cell = worksheet4['E34']  
    text_cell.value = obj.Facade_2_Mitoyennete
    text_cell = worksheet4['E35'] 
    text_cell.value = f"Longueur = {obj.Facade_2_Longueur}"
    text_cell = worksheet4['E36']  
    text_cell.value = f"Hauteur = {obj.Facade_2_Hauteur}"
    text_cell = worksheet4['E37']  
    text_cell.value = f"Surface = {obj.Facade_2_Surface}"
    
    image_cell_1 = worksheet4['E38']  
    image_cell_1.value = None
    if obj.Facade_2_Photo_Principale:
        image_path_ = obj.Facade_2_Photo_Principale.path  # Get the file path
        if default_storage.exists(image_path_):
            image_path1 = obj.Facade_2_Photo_Principale.path
            img_1 = Image(image_path1)
            img_1.width =  185.28 #cell_width
            img_1.height = 140.16 # cell_height
            worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    
    
    text_cell = worksheet4['A46']  
    text_cell.value = obj.Facade_3_Orientation
    #text_cell = worksheet4['A4']  
    #text_cell.value = obj.Facade_3_Mitoyennete
    text_cell = worksheet4['A47'] 
    text_cell.value = f"Longueur = {obj.Facade_3_Longueur}"
    text_cell = worksheet4['A48']  
    text_cell.value = f"Hauteur = {obj.Facade_3_Hauteur}"
    text_cell = worksheet4['A49']  
    text_cell.value = f"Surface = {obj.Facade_3_Surface}"
    
    image_cell_1 = worksheet4['A50'] 
    image_cell_1.value = None
    #image_cell_1.hyperlink = None
    if obj.Facade_3_Photo_Principale:
        image_path_ = obj.Facade_3_Photo_Principale.path  # Get the file path
        if default_storage.exists(image_path_):
            image_path1 = obj.Facade_3_Photo_Principale.path
            img_1 = Image(image_path1)
            img_1.width =  185.28 #cell_width
            img_1.height = 140.16 # cell_height
            worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    
    
    text_cell = worksheet4['E46']  
    text_cell.value = obj.Facade_4_Orientation
    #text_cell = worksheet4['E34']  
    #text_cell.value = obj.Facade_4_Mitoyennete
    text_cell = worksheet4['E47'] 
    text_cell.value = f"Longueur = {obj.Facade_4_Longueur}"
    text_cell = worksheet4['E48']  
    text_cell.value = f"Hauteur = {obj.Facade_4_Hauteur}"
    text_cell = worksheet4['E49']  
    text_cell.value = f"Surface = {obj.Facade_4_Surface}"
    
    image_cell_1 = worksheet4['E50'] 
    image_cell_1.value = None
    if obj.Facade_4_Photo_Principale:
        image_path_ = obj.Facade_4_Photo_Principale.path  # Get the file path
        if default_storage.exists(image_path_):
            image_path1 = obj.Facade_4_Photo_Principale.path
            img_1 = Image(image_path1)
            img_1.width =  185.28 #cell_width
            img_1.height = 140.16 # cell_height
            worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    ################################### end Facade
    
    
    
    
    
    
    
    ######################################   END WORK_SHEET_4
    ######################################   END WORK_SHEET_4
    ######################################   END WORK_SHEET_4
    
        ###################################################### save process #######################################################
    # Save the updated XLSX file temporarily
    temp_xlsx_path = 'path_to_temp_xlsx.xlsx'  # Provide a temporary path on your server
    workbook.save(temp_xlsx_path)
    if UpdatedXLSXFile.objects.filter(name=file_id) :
        pass
    else:
        UpdatedXLSXFile.objects.create(name=file_id)
    # Create a new instance of your other model
    updated_xlsx = UpdatedXLSXFile.objects.get(name=file_id)

    # Assign the XLSX file to the FileField or ImageField of the new model instance
    updated_xlsx.xlsx_file.save( 'updated_template.xlsx', open(temp_xlsx_path, 'rb'))

    # Save the new model instance to persist the XLSX file
    updated_xlsx.save()

    
        
        
        
    # Fetch the MyFile object by its ID
    my_file = get_object_or_404(UpdatedXLSXFile, name=file_id)

    # Open the file and create an HttpResponse with the file's content
    with my_file.xlsx_file.open('rb') as f:
        response = HttpResponse(f.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{my_file.xlsx_file.name}"'
        return response
    pass