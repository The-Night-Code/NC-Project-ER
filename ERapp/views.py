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
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import random
import string
from datetime import datetime

import openpyxl
from openpyxl.utils import get_column_letter
from openpyxl.drawing.image import Image
from io import BytesIO

from django.http import HttpResponse
from .models import MyModel, UpdatedXLSXFile 
from openpyxl.styles import NamedStyle


formT="/formT/"
link2="/agentimmo/"
VT="/VT/"
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
       
    
def chat_box_1(request):
    cell_id = request.GET.get('param0')
    
    user_email = request.GET.get('param1')
    user_firstname = request.GET.get('param2')
    user_lastname = request.GET.get('param3')
    box = request.GET.get('param4')
    msg = request.GET.get('param5')
    
    msg_id =generate_random_string(8)
    

    if msg and not str.isspace(msg) : 
        message_box_1.objects.create(
                    message_id = msg_id,
                    row_id = cell_id,
                    username =user_firstname + " , " +  user_lastname,
                    email =  user_email,
                    message =msg,
                    box =box
                )
    
        
    return redirect(formT)

    
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


def VT_Page(request):

    
    data = TableData001.objects.all()
    return render(request, 'html/VTPage.html', { 'data': data })

def VT_Page_edit_state(request):
    param_value_id = request.GET.get('param0')
    etat_vt_value = request.GET.get('param1')
    
    try:
        object = TableData001.objects.get(cell_id=str(param_value_id))
        object.etat_vt =  etat_vt_value
        object.save(update_fields=['etat_vt'])

    except TableData001.DoesNotExist:
        pass
    
    
    return redirect(VT)


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
        
        myButton = request.POST.get("mybutton1")
        if myButton=="mybutton1":
            #return redirect(formT)
            input_cell_name = request.POST.get("input_value")
            img_get= request.FILES[input_cell_name]
        
            if hasattr(obj, input_cell_name):
                # Check if the field exists in the model
                setattr(obj, input_cell_name, img_get)
                obj.save()        
        
        
        submit_to_Kizeo = request.POST.get("submit_to_Kizeo")
        if submit_to_Kizeo=="submit":
            #obj.signature_data = request.FILES.get('signatureData')
            
            ### Données Générales
            obj.latitude = request.POST.get("latitude")
            obj.longitude = request.POST.get("longitude")
            obj.altitude = request.POST.get("altitude")
            obj.Donnees_Generales_Nom_d_intervenant = request.POST.get("Donnees_Generales_Nom_d_intervenant")
            
            Donnees_Generales_Date_de_visite = request.POST.get("Donnees_Generales_Date_de_visite")
            obj.Donnees_Generales_Date_de_visite = datetime.strptime(Donnees_Generales_Date_de_visite,'%Y-%m-%d')
            
            obj.Donnees_Generales_Adresse = request.POST.get("Donnees_Generales_Adresse")
            obj.Donnees_Generales_Zip_Code = int(request.POST.get("Donnees_Generales_Zip_Code"))
            obj.Donnees_Generales_City = request.POST.get("Donnees_Generales_City")
            obj.Donnees_Generales_Annee_de_construction = request.POST.get("Donnees_Generales_Annee_de_construction")
            obj.Donnees_Generales_Etat_d_occupation = request.POST.get("Donnees_Generales_Etat_d_occupation")
            obj.Donnees_Generales_Nom_client = request.POST.get("Donnees_Generales_Nom_client")
            obj.Donnees_Generales_Tel_client = int(request.POST.get("Donnees_Generales_Tel_client"))
            obj.Donnees_Generales_Email = request.POST.get("Donnees_Generales_Email")
            obj.Donnees_Generales_Horaire_d_occupation_des_lieux = request.POST.get("Donnees_Generales_Horaire_d_occupation_des_lieux")
            obj.Donnees_Generales_Destination_du_lieu = request.POST.get("Donnees_Generales_Destination_du_lieu")
            obj.Donnees_Generales_Nombre_d_occupant = int(request.POST.get("Donnees_Generales_Nombre_d_occupant"))
            obj.Donnees_Generales_Nombre_de_niveau = int(request.POST.get("Donnees_Generales_Nombre_de_niveau"))
            obj.Donnees_Generales_Surface_TOTALE = int(request.POST.get("Donnees_Generales_Surface_TOTALE"))
            obj.Donnees_Generales_Preuve_Surface = request.POST.get("Donnees_Generales_Preuve_Surface")
            obj.Donnees_Generales_Surface_ajoute_depuis_moins_de_15_ans = int(request.POST.get("Donnees_Generales_Surface_ajoute_depuis_moins_de_15_ans"))
            obj.Donnees_Generales_Besoin_du_client_Chauffage = request.POST.get("Donnees_Generales_Besoin_du_client_Chauffage")
            obj.Donnees_Generales_Besoin_du_client_Isolation = request.POST.get("Donnees_Generales_Besoin_du_client_Isolation")
            obj.Donnees_Generales_Scenario_souhaite_par_le_client = request.POST.get("Donnees_Generales_Scenario_souhaite_par_le_client")
            
            ### Façades
            obj.Facade_1_Orientation = request.POST.get("Facade_1_Orientation")
            obj.Facade_1_Mitoyennete = request.POST.get("Facade_1_Mitoyennete")
            obj.Facade_1_Longueur = float(request.POST.get("Facade_1_Longueur"))
            obj.Facade_1_Hauteur = float(request.POST.get("Facade_1_Hauteur"))
            obj.Facade_1_Surfac = float(request.POST.get("Facade_1_Longueur")) * float(request.POST.get("Facade_1_Hauteur"))
            #Facade_1_Photo_Principale = request.FILES['Facade_1_Photo_Principale']
            
            obj.Facade_2_Orientation = request.POST.get("Facade_2_Orientation")
            obj.Facade_2_Mitoyennete = request.POST.get("Facade_2_Mitoyennete")
            obj.Facade_2_Longueur = float(request.POST.get("Facade_2_Longueur"))
            obj.Facade_2_Hauteur = float(request.POST.get("Facade_2_Hauteur"))
            obj.Facade_2_Surfac = (float(request.POST.get("Facade_2_Longueur")) * float(request.POST.get("Facade_2_Hauteur")))
            #Facade_2_Photo_Principale = request.FILES['Facade_2_Photo_Principale']
            
            obj.Facade_3_Orientation = request.POST.get("Facade_3_Orientation")
            obj.Facade_3_Mitoyennete = request.POST.get("Facade_3_Mitoyennete")
            obj.Facade_3_Longueur = float(request.POST.get("Facade_3_Longueur"))
            obj.Facade_3_Hauteur = float(request.POST.get("Facade_3_Hauteur"))
            obj.Facade_3_Surfac = (float(request.POST.get("Facade_3_Longueur")) * float(request.POST.get("Facade_3_Hauteur")))
            #Facade_3_Photo_Principale = request.FILES['Facade_3_Photo_Principale']
            
            obj.Facade_4_Orientation = request.POST.get("Facade_4_Orientation")
            obj.Facade_4_Mitoyennete = request.POST.get("Facade_4_Mitoyennete")
            obj.Facade_4_Longueur = float(request.POST.get("Facade_4_Longueur"))
            obj.Facade_4_Hauteur = float(request.POST.get("Facade_4_Hauteur"))
            obj.Facade_4_Surfac = (float(request.POST.get("Facade_4_Longueur")) * float(request.POST.get("Facade_4_Hauteur")))
            #Facade_4_Photo_Principale = request.FILES['Facade_4_Photo_Principale']
            
            
            ### Cauffage
            obj.Cauffage_systeme = request.POST.get("Cauffage_systeme")
            obj.Cauffage_annee_de_mise_en_oeuvre = int(request.POST.get("Cauffage_annee_de_mise_en_oeuvre"))
            #Cauffage_photo_systeme_de_production = request.FILES['Cauffage_photo_systeme_de_production']
            #Cauffage_photo_fiche_signaletique = request.FILES['Cauffage_photo_fiche_signaletique']
            obj.Cauffage_type_de_regulation = request.POST.get("Cauffage_type_de_regulation")
            obj.Cauffage_system_d_appoint = request.POST.get("Cauffage_system_d_appoint")
            #Cauffage_photo_appoint = request.FILES['Cauffage_photo_appoint']
            obj.Cauffage_commentaire = request.POST.get("Cauffage_commentaire")
                
            ### ECS
            obj.ECS_type =request.POST.get("ECS_type")
            obj.ECS_system_d_appoint = request.POST.get("ECS_system_d_appoint")
            #ECS_photo_appoint = request.FILES['ECS_photo_appoint']
            obj.ECS_commentaire = request.POST.get("ECS_commentaire")

            ### Ventilation
            obj.Ventilation_type = request.POST.get("Ventilation_type")
            #Ventilation_photo_ventilation = request.FILES['Ventilation_photo_ventilation']
            
            ### Refroidissement
            obj.Refroidissement_type = request.POST.get("Refroidissement_type")
            obj.Refroidissement_commentaire = request.POST.get("Refroidissement_commentaire")
            
            ### Compteur Electrique
            obj.Compteur_Electrique_Puissance_souscrite = float(request.POST.get("Compteur_Electrique_Puissance_souscrite"))
            obj.Compteur_Electrique_type = request.POST.get("Compteur_Electrique_type")
            #Compteur_Electrique_photo_compteur = request.FILES['Compteur_Electrique_photo_compteur']
            obj.Compteur_Electrique_commentaire = request.POST.get("Compteur_Electrique_commentaire")
            
            ### Mur 1
            obj.Mur_1_Position = request.POST.get("Mur_1_Position")
            obj.Mur_1_Composition = request.POST.get("Mur_1_Composition")
            obj.Mur_1_Epaisseur_mur = request.POST.get("Mur_1_Epaisseur_mur")
            obj.Mur_1_Isolation = request.POST.get("Mur_1_Isolation")
            obj.Mur_1_Epaisseur_isolant = request.POST.get("Mur_1_Epaisseur_isolant")
            obj.Mur_1_Date_d_isolation = request.POST.get("Mur_1_Date_d_isolation")
            obj.Mur_1_Preuve_d_isolation = request.POST.get("Mur_1_Preuve_d_isolation")
            #obj.Mur_1_Photo_mur = request.FILES['Mur_1_Photo_mur']
            
            ### Mur 1
            obj.Mur_2_Position = request.POST.get("Mur_2_Position")
            obj.Mur_2_Composition = request.POST.get("Mur_2_Composition")
            obj.Mur_2_Epaisseur_mur = request.POST.get("Mur_2_Epaisseur_mur")
            obj.Mur_2_Isolation = request.POST.get("Mur_2_Isolation")
            obj.Mur_2_Epaisseur_isolant = request.POST.get("Mur_2_Epaisseur_isolant")
            obj.Mur_2_Date_d_isolation = request.POST.get("Mur_2_Date_d_isolation")
            obj.Mur_2_Preuve_d_isolation = request.POST.get("Mur_2_Preuve_d_isolation")
            
            
            ### Plancher bas 1
            obj.Plancher_bas_1_Position = request.POST.get("Plancher_bas_1_Position")
            obj.Plancher_bas_1_Composition = request.POST.get("Plancher_bas_1_Composition")
            obj.Plancher_bas_1_Surface = float(request.POST.get("Plancher_bas_1_Surface"))
            obj.Plancher_bas_1_Isolation = request.POST.get("Plancher_bas_1_Isolation")
            obj.Plancher_bas_1_Epaisseur_isolant = float(request.POST.get("Plancher_bas_1_Epaisseur_isolant"))
            obj.Plancher_bas_1_Date_d_isolation = request.POST.get("Plancher_bas_1_Date_d_isolation")
            obj.Plancher_bas_1_Preuve_d_isolation = request.POST.get("Plancher_bas_1_Preuve_d_isolation")
            #obj.Plancher_bas_1_Photo_plancher_bas = 
            
            ### Plancher bas 2
            obj.Plancher_bas_2_Position = request.POST.get("Plancher_bas_2_Position")
            obj.Plancher_bas_2_Composition = request.POST.get("Plancher_bas_2_Composition")
            obj.Plancher_bas_2_Surface = float(request.POST.get("Plancher_bas_2_Surface"))
            obj.Plancher_bas_2_Isolation = request.POST.get("Plancher_bas_2_Isolation")
            obj.Plancher_bas_2_Epaisseur_isolant = float(request.POST.get("Plancher_bas_2_Epaisseur_isolant"))
            obj.Plancher_bas_2_Date_d_isolation = request.POST.get("Plancher_bas_2_Date_d_isolation")
            obj.Plancher_bas_2_Preuve_d_isolation = request.POST.get("Plancher_bas_2_Preuve_d_isolation")
            #obj.Plancher_bas_2_Photo_plancher_bas = 
            
             ### Plancher bas 1
            obj.Plancher_Haut_1_Type = request.POST.get("Plancher_Haut_1_Type")
            obj.Plancher_Haut_1_Composition = request.POST.get("Plancher_Haut_1_Composition")
            obj.Plancher_Haut_1_Surface = float(request.POST.get("Plancher_Haut_1_Surface"))
            obj.Plancher_Haut_1_Isolation = request.POST.get("Plancher_Haut_1_Isolation")
            obj.Plancher_Haut_1_Epaisseur_isolant = float(request.POST.get("Plancher_Haut_1_Epaisseur_isolant"))
            obj.Plancher_Haut_1_Date_d_isolation = request.POST.get("Plancher_Haut_1_Date_d_isolation")
            obj.Plancher_Haut_1_Preuve_d_isolation = request.POST.get("Plancher_Haut_1_Preuve_d_isolation")
            #obj.Plancher_bas_1_Photo_plancher_bas = 
            
            ### Plancher bas 2
            obj.Plancher_Haut_2_Type = request.POST.get("Plancher_Haut_2_Type")
            obj.Plancher_Haut_2_Composition = request.POST.get("Plancher_Haut_2_Composition")
            obj.Plancher_Haut_2_Surface = float(request.POST.get("Plancher_Haut_2_Surface"))
            obj.Plancher_Haut_2_Isolation = request.POST.get("Plancher_Haut_2_Isolation")
            obj.Plancher_Haut_2_Epaisseur_isolant = float(request.POST.get("Plancher_Haut_2_Epaisseur_isolant"))
            obj.Plancher_Haut_2_Date_d_isolation = request.POST.get("Plancher_Haut_2_Date_d_isolation")
            obj.Plancher_Haut_2_Preuve_d_isolation = request.POST.get("Plancher_Haut_2_Preuve_d_isolation")
            #obj.Plancher_bas_2_Photo_plancher_bas = 
            
            ### Fenetre type 1
            obj.Fenetre_type_1_Menuiserie = request.POST.get("Fenetre_type_1_Menuiserie")
            obj.Fenetre_type_1_Materiaux = request.POST.get("Fenetre_type_1_Materiaux")
            obj.Fenetre_type_1_Type_de_vitrage = request.POST.get("Fenetre_type_1_Type_de_vitrage")
            obj.Fenetre_type_1_Volets = request.POST.get("Fenetre_type_1_Volets")
            obj.Fenetre_type_1_Nombre = int(request.POST.get("Fenetre_type_1_Nombre"))

            ### Fenetre type 2
            obj.Fenetre_type_2_Menuiserie = request.POST.get("Fenetre_type_2_Menuiserie")
            obj.Fenetre_type_2_Materiaux = request.POST.get("Fenetre_type_2_Materiaux")
            obj.Fenetre_type_2_Type_de_vitrage = request.POST.get("Fenetre_type_2_Type_de_vitrage")
            obj.Fenetre_type_2_Volets = request.POST.get("Fenetre_type_2_Volets")
            obj.Fenetre_type_2_Nombre = int(request.POST.get("Fenetre_type_2_Nombre"))
            
            ### Porte 1
            obj.Porte_1_Materiaux = request.POST.get("Porte_1_Materiaux")
            obj.Porte_1_Type_porte = request.POST.get("Porte_1_Type_porte")
            obj.Porte_1_Nombre = float(request.POST.get("Porte_1_Nombre"))
            
            ### Porte 2
            obj.Porte_2_Materiaux = request.POST.get("Porte_2_Materiaux")
            obj.Porte_2_Type_porte = request.POST.get("Porte_2_Type_porte")
            obj.Porte_2_Nombre = float(request.POST.get("Porte_2_Nombre"))
            
            
            obj.save(update_fields=[
                                    ### Données Générales
                                    'latitude',
                                    'longitude',
                                    'altitude',
                                    'Donnees_Generales_Nom_d_intervenant',
                                    'Donnees_Generales_Date_de_visite',
                                    'Donnees_Generales_Adresse',
                                    'Donnees_Generales_Zip_Code',
                                    'Donnees_Generales_City',
                                    'Donnees_Generales_Annee_de_construction',
                                    'Donnees_Generales_Etat_d_occupation',
                                    'Donnees_Generales_Nom_client',
                                    'Donnees_Generales_Tel_client',
                                    'Donnees_Generales_Email',
                                    'Donnees_Generales_Horaire_d_occupation_des_lieux',
                                    'Donnees_Generales_Destination_du_lieu',
                                    'Donnees_Generales_Nombre_d_occupant',
                                    'Donnees_Generales_Nombre_de_niveau',
                                    'Donnees_Generales_Surface_TOTALE',
                                    'Donnees_Generales_Preuve_Surface',
                                    'Donnees_Generales_Surface_ajoute_depuis_moins_de_15_ans',
                                    'Donnees_Generales_Besoin_du_client_Chauffage',
                                    'Donnees_Generales_Besoin_du_client_Isolation',
                                    'Donnees_Generales_Scenario_souhaite_par_le_client',
                                    
                                    ### Façades
                                    'Facade_1_Orientation', 'Facade_1_Mitoyennete','Facade_1_Longueur','Facade_1_Hauteur','Facade_1_Surface',#'Facade_1_Photo_Principale',
                                    'Facade_2_Orientation', 'Facade_2_Mitoyennete','Facade_2_Longueur','Facade_2_Hauteur','Facade_2_Surface',#'Facade_2_Photo_Principale',
                                    'Facade_3_Orientation', 'Facade_3_Mitoyennete','Facade_3_Longueur','Facade_3_Hauteur','Facade_3_Surface',#'Facade_3_Photo_Principale',
                                    'Facade_4_Orientation', 'Facade_4_Mitoyennete','Facade_4_Longueur','Facade_4_Hauteur','Facade_4_Surface',#'Facade_4_Photo_Principale',
                                     
                                    ### Cauffage
                                    "Cauffage_systeme",
                                    "Cauffage_annee_de_mise_en_oeuvre",
                                    "Cauffage_type_de_regulation",
                                    "Cauffage_system_d_appoint",
                                    "Cauffage_commentaire" ,
                                    
                                    ### ECS
                                    "ECS_type",
                                    "ECS_system_d_appoint",
                                    "ECS_commentaire",
                                    
                                    ### Ventilation
                                    "Ventilation_type" ,
                                    
                                    ### Refroidissement
                                    "Refroidissement_type" ,
                                    "Refroidissement_commentaire" ,
                                    
                                    ### Compteur Electrique
                                    "Compteur_Electrique_Puissance_souscrite" ,
                                    "Compteur_Electrique_type" ,
                                    "Compteur_Electrique_commentaire" ,
                                    
                                    ### Mur 1
                                    "Mur_1_Position", 
                                    "Mur_1_Composition",
                                    "Mur_1_Epaisseur_mur",
                                    "Mur_1_Isolation",
                                    "Mur_1_Epaisseur_isolant",
                                    "Mur_1_Date_d_isolation",
                                    "Mur_1_Preuve_d_isolation",
                                    ### Mur 2
                                    "Mur_2_Position", 
                                    "Mur_2_Composition",
                                    "Mur_2_Epaisseur_mur",
                                    "Mur_2_Isolation",
                                    "Mur_2_Epaisseur_isolant",
                                    "Mur_2_Date_d_isolation",
                                    "Mur_2_Preuve_d_isolation",
                                    
                                    ### Plancher bas 1
                                    "Plancher_bas_1_Position",
                                    "Plancher_bas_1_Composition" ,
                                    "Plancher_bas_1_Isolation" ,
                                    "Plancher_bas_1_Epaisseur_isolant" ,
                                    "Plancher_bas_1_Date_d_isolation" ,
                                    "Plancher_bas_1_Preuve_d_isolation" ,
                                    "Plancher_bas_1_Photo_plancher_bas" ,
                                    ### Plancher bas 2
                                    "Plancher_bas_2_Position",
                                    "Plancher_bas_2_Composition" ,
                                    "Plancher_bas_2_Isolation" ,
                                    "Plancher_bas_2_Epaisseur_isolant" ,
                                    "Plancher_bas_2_Date_d_isolation" ,
                                    "Plancher_bas_2_Preuve_d_isolation" ,
                                    "Plancher_bas_2_Photo_plancher_bas" ,
                                    
                                    ### Plancher haut 1
                                    "Plancher_Haut_1_Type",
                                    "Plancher_Haut_1_Composition",
                                    "Plancher_Haut_1_Surface",
                                    "Plancher_Haut_1_Isolation" ,
                                    "Plancher_Haut_1_Epaisseur_isolant" ,
                                    "Plancher_Haut_1_Date_d_isolation",
                                    "Plancher_Haut_1_Preuve_d_isolation" ,
                                    "Plancher_Haut_1_Photo_plancher_bas" ,
                                    ### Plancher haut 2
                                    "Plancher_Haut_2_Type",
                                    "Plancher_Haut_2_Composition",
                                    "Plancher_Haut_2_Surface",
                                    "Plancher_Haut_2_Isolation" ,
                                    "Plancher_Haut_2_Epaisseur_isolant" ,
                                    "Plancher_Haut_2_Date_d_isolation",
                                    "Plancher_Haut_2_Preuve_d_isolation" ,
                                    "Plancher_Haut_2_Photo_plancher_bas" ,
                                    
                                    
                                    ### Fenetre type 1
                                    "Fenetre_type_1_Menuiserie" ,
                                    "Fenetre_type_1_Materiaux",
                                    "Fenetre_type_1_Type_de_vitrage" ,
                                    "Fenetre_type_1_Volets" ,
                                    "Fenetre_type_1_Nombre",
                                    "Fenetre_type_1_Photo" ,
                                    ### Fenetre type 2
                                    "Fenetre_type_2_Menuiserie" ,
                                    "Fenetre_type_2_Materiaux",
                                    "Fenetre_type_2_Type_de_vitrage" ,
                                    "Fenetre_type_2_Volets" ,
                                    "Fenetre_type_2_Nombre",
                                    "Fenetre_type_2_Photo" ,
                                    
                                    ### Porte 1
                                    "Porte_1_Materiaux",
                                    "Porte_1_Type_porte",
                                    "Porte_1_Nombre",
                                    ### Porte 2
                                    "Porte_2_Materiaux",
                                    "Porte_2_Type_porte",
                                    "Porte_2_Nombre",
                                    

                                    #'signature_data',

                                ])

    data = kizeo_model.objects.get(kizeo_id=client_id)
    return render(request, 'html/formK.html',{"data":data})



def save_signature(request):
    if request.method == 'POST':
        return redirect("gggg")
        signature_data = request.POST.get('signature', '')

        # You can save the signature data to your model as an image field.
        # Here, assume you have a model named Signature with a signature field.
        obj = kizeo_model.objects.get(kizeo_id="4MLJMq2cj8")
        obj.objects.create(signature_image=signature_data)
        return JsonResponse({'message': 'Signature saved successfully.'})

    
    
def download_K_file(request,file_id):
    if kizeo_model.objects.filter(kizeo_id=file_id):
            pass
    else:
        kizeo_model.objects.create(kizeo_id=file_id)
    
    obj = kizeo_model.objects.get(kizeo_id=file_id)
    template_path = 'ERapp\static\KiFile.xlsx'  # Provide the path to your template file
    workbook = openpyxl.load_workbook(template_path)
    
    worksheet1 = workbook["Données"]
    worksheet2 = workbook["Métré"]
    worksheet3 = workbook["Garde"]
    worksheet4 = workbook["Site"]
    
    ###################################### start WORK_SHEET_1
    ###################################### start WORK_SHEET_1
    ###################################### start WORK_SHEET_1
    i=2
    text_cell = worksheet1[f'B{i}']  
    text_cell.value = obj.Donnees_Generales_Nom_d_intervenant
    i+=1#3
    text_cell = worksheet1[f'B{i}']  
    text_cell.value = obj.Donnees_Generales_Date_de_visite
    i+=1#4
    text_cell = worksheet1[f'B{i}']  
    text_cell.value = obj.Donnees_Generales_Adresse
    i+=1#5
    text_cell = worksheet1[f'B{i}']  
    text_cell.value = obj.Donnees_Generales_Zip_Code
    i+=1#6
    text_cell = worksheet1[f'B{i}']  
    text_cell.value = obj.Donnees_Generales_City
    i+=1#7
    text_cell = worksheet1[f'B{i}']  
    text_cell.value = obj.Donnees_Generales_Annee_de_construction
    i+=1#8
    text_cell = worksheet1[f'B{i}']  
    text_cell.value = obj.Donnees_Generales_Nom_client
    i+=1#9
    text_cell = worksheet1[f'B{i}']  
    text_cell.value = obj.Donnees_Generales_Tel_client
    i+=1#10
    text_cell = worksheet1[f'B{i}']  
    text_cell.value = obj.Donnees_Generales_Email
    i+=1#11
    text_cell = worksheet1[f'B{i}']  
    text_cell.value = "obj."
    i+=1#12
    text_cell = worksheet1[f'B{i}']  
    text_cell.value = "obj."
    i+=1#13
    text_cell = worksheet1[f'B{i}']  
    text_cell.value = obj.Donnees_Generales_Nombre_d_occupant
    i+=1#14
    text_cell = worksheet1[f'B{i}']  
    text_cell.value = obj.Donnees_Generales_Surface_TOTALE
    i+=1#15
    text_cell = worksheet1[f'B{i}']  
    text_cell.value = obj.Donnees_Generales_Preuve_Surface
    i+=1#16
    text_cell = worksheet1[f'B{i}']  
    text_cell.value = obj.Donnees_Generales_Surface_ajoute_depuis_moins_de_15_ans
    
    
    
    ###################################### end WORK_SHEET_1
    ###################################### end WORK_SHEET_1
    ###################################### end WORK_SHEET_1
    
    
    ###################################### start WORK_SHEET_2
    ###################################### start WORK_SHEET_2
    ###################################### start WORK_SHEET_2
    
    ###################################### end WORK_SHEET_2
    ###################################### end WORK_SHEET_2
    ###################################### end WORK_SHEET_2
    
    
    ###################################### start WORK_SHEET_3
    ###################################### start WORK_SHEET_3
    ###################################### start WORK_SHEET_3
    image_cell_1 = worksheet3['B6'] 
    image_cell_1.value = None
    o = obj.Donnees_Generales_Preuve_Surface_Photo
    if o:
        image_path_ = o.path  # Get the file path
        if default_storage.exists(image_path_):
            image_path1 = o.path
            img_1 = Image(image_path1)
            img_1.width =  382.08 #cell_width 3.98
            img_1.height = 280.32 # cell_height 2.92
            worksheet3.add_image(img_1, image_cell_1.coordinate)
            
    i=26
    text_cell = worksheet3[f'B{i}']  
    text_cell.value = obj.Donnees_Generales_Nom_client
    i+=1
    text_cell = worksheet3[f'B{i}']  
    text_cell.value = obj.Donnees_Generales_Adresse
    i+=1
    text_cell = worksheet3[f'B{i}']  
    text_cell.value = obj.Donnees_Generales_Zip_Code
    i+=1
    text_cell = worksheet3[f'B{i}']  
    text_cell.value = obj.Donnees_Generales_City
    
    text_cell = worksheet3['C33']  
    text_cell.value = obj.Donnees_Generales_Date_de_visite
    ###################################### end WORK_SHEET_3
    ###################################### end WORK_SHEET_3
    ###################################### end WORK_SHEET_3
    
    ################################### start WORK_SHEET_4
    ################################### start WORK_SHEET_4
    ################################### start WORK_SHEET_4
    text_cell = worksheet4['A7']
    text_cell.value =f"L'audit énergétique est réalisé une maison individuelle située à {obj.Donnees_Generales_Adresse}, {obj.Donnees_Generales_Zip_Code} {obj.Donnees_Generales_City}."
    
    text_cell = worksheet4['E27']  
    text_cell.value = obj.Donnees_Generales_Annee_de_construction
    text_cell = worksheet4['E28']  
    text_cell.value = obj.Donnees_Generales_Etat_d_occupation
    text_cell = worksheet4['E29'] 
    text_cell.value = obj.Donnees_Generales_Surface_TOTALE
    
    
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
    
    
    
    
    ### mur 1
    #text_cell1 = worksheet4.merge_cells('B60:E60') 
    #cell = text_cell1.cell(row=1, column=1) 
    text_cell = worksheet4['B60'] 
    text_cell.value = f"Murs - type 1 - {obj.Mur_1_Position}"
    text_cell = worksheet4['E61']  
    text_cell.value = obj.Mur_1_Composition
    text_cell = worksheet4['E62'] 
    text_cell.value = obj.Mur_1_Epaisseur_mur
    text_cell = worksheet4['E63']  
    text_cell.value = obj.Mur_1_Isolation
    text_cell = worksheet4['E64']  
    text_cell.value = obj.Mur_1_Epaisseur_isolant
    text_cell = worksheet4['E65']  
    text_cell.value = obj.Mur_1_Date_d_isolation
    text_cell = worksheet4['E66']  
    #text_cell.value = obj.
    
    image_cell_1 = worksheet4['B67'] 
    image_cell_1.value = None
    if obj.Mur_1_Photo_mur:
        image_path_ = obj.Mur_1_Photo_mur.path  # Get the file path
        if default_storage.exists(image_path_):
            image_path1 = obj.Mur_1_Photo_mur.path
            img_1 = Image(image_path1)
            img_1.width =  185.28 #cell_width
            img_1.height = 140.16 # cell_height
            worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    
    ### mur 2
    #text_cell1 = worksheet4.merge_cells('B60:E60') 
    #cell = text_cell1.cell(row=1, column=1) 
    text_cell = worksheet4['B76'] 
    text_cell.value = f"Murs - type 2 - {obj.Mur_2_Position}"
    text_cell = worksheet4['E77']  
    text_cell.value = obj.Mur_2_Composition
    text_cell = worksheet4['E78'] 
    text_cell.value = obj.Mur_2_Epaisseur_mur
    text_cell = worksheet4['E79']  
    text_cell.value = obj.Mur_2_Isolation
    text_cell = worksheet4['E80']  
    text_cell.value = obj.Mur_2_Epaisseur_isolant
    text_cell = worksheet4['E81']  
    text_cell.value = obj.Mur_2_Date_d_isolation
    text_cell = worksheet4['E82']  
    #text_cell.value = obj.
    
    image_cell_1 = worksheet4['B83'] 
    image_cell_1.value = None
    if obj.Mur_2_Photo_mur:
        image_path_ = obj.Mur_2_Photo_mur.path  # Get the file path
        if default_storage.exists(image_path_):
            image_path1 = obj.Mur_2_Photo_mur.path
            img_1 = Image(image_path1)
            img_1.width =  185.28 #cell_width
            img_1.height = 140.16 # cell_height
            worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    
    
    
    ### Plancher bas type1
    text_cell = worksheet4['E92'] 
    text_cell.value = obj.Plancher_bas_1_Position
    text_cell = worksheet4['E93']  
    text_cell.value = obj.Plancher_bas_1_Composition
    text_cell = worksheet4['E94'] 
    text_cell.value = obj.Plancher_bas_1_Isolation
    text_cell = worksheet4['E95']  
    text_cell.value = obj.Plancher_bas_1_Epaisseur_isolant
    text_cell = worksheet4['E96']  
    text_cell.value = obj.Plancher_bas_1_Date_d_isolation
    text_cell = worksheet4['E97']  
    text_cell.value = obj.Plancher_bas_1_Surface
    text_cell = worksheet4['E98']  
    #text_cell.value = obj.
    
    image_cell_1 = worksheet4['B99'] 
    image_cell_1.value = None
    if obj.Plancher_bas_1_Photo_plancher_bas:
        image_path_ = obj.Plancher_bas_1_Photo_plancher_bas.path  # Get the file path
        if default_storage.exists(image_path_):
            image_path1 = obj.Plancher_bas_1_Photo_plancher_bas.path
            img_1 = Image(image_path1)
            img_1.width =  185.28 #cell_width
            img_1.height = 140.16 # cell_height
            worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    
    ################################### end Facade
    
    ### Plancher bas type1
    j=108
    for i in [obj.Plancher_bas_2_Position,obj.Plancher_bas_2_Composition,obj.Plancher_bas_2_Isolation
              ,obj.Plancher_bas_2_Epaisseur_isolant,obj.Plancher_bas_2_Date_d_isolation,obj.Plancher_bas_2_Surface]:
        
        text_cell = worksheet4[f'E{j}'] 
        text_cell.value = i
        j+=1
        
    image_cell_1 = worksheet4['B115'] 
    image_cell_1.value = None
    if obj.Plancher_bas_2_Photo_plancher_bas:
        image_path_ = obj.Plancher_bas_2_Photo_plancher_bas.path  # Get the file path
        if default_storage.exists(image_path_):
            image_path1 = obj.Plancher_bas_2_Photo_plancher_bas.path
            img_1 = Image(image_path1)
            img_1.width =  185.28 #cell_width
            img_1.height = 140.16 # cell_height
            worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    ### Plancher haut type1
    j=124
    for i in [obj.Plancher_Haut_1_Type,obj.Plancher_Haut_1_Composition,obj.Plancher_Haut_1_Isolation
              ,obj.Plancher_Haut_1_Epaisseur_isolant,obj.Plancher_Haut_1_Date_d_isolation,obj.Plancher_Haut_1_Surface]:
        
        text_cell = worksheet4[f'E{j}'] 
        text_cell.value = i
        j+=1
        
    objimage =obj.Plancher_Haut_1_Photo_plancher_bas
    image_cell_1 = worksheet4['B131'] 
    image_cell_1.value = None
    if objimage:
        image_path_ =objimage.path  # Get the file path
        if default_storage.exists(image_path_):
            image_path1 = objimage.path
            img_1 = Image(image_path1)
            img_1.width =  185.28 #cell_width
            img_1.height = 140.16 # cell_height
            worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    
    ### Plancher haut type 2
    j=140
    for i in [obj.Plancher_Haut_2_Type,obj.Plancher_Haut_2_Composition,obj.Plancher_Haut_2_Isolation
              ,obj.Plancher_Haut_2_Epaisseur_isolant,obj.Plancher_Haut_2_Date_d_isolation,obj.Plancher_Haut_2_Surface]:
        
        text_cell = worksheet4[f'E{j}'] 
        text_cell.value = i
        j+=1
        
    objimage =obj.Plancher_Haut_2_Photo_plancher_bas
    image_cell_1 = worksheet4['B147'] 
    image_cell_1.value = None
    if objimage:
        image_path_ =objimage.path  # Get the file path
        if default_storage.exists(image_path_):
            image_path1 = objimage.path
            img_1 = Image(image_path1)
            img_1.width =  185.28 #cell_width
            img_1.height = 140.16 # cell_height
            worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    
    ### Fenêtre 1
    text_cell = worksheet4[f'B155'] 
    text_cell.value = obj.Fenetre_type_1_Menuiserie
    j=156
    
    text_cell = worksheet4[f'E{j}'] 
    text_cell.value = obj.Fenetre_type_1_Materiaux
    j+1
    text_cell = worksheet4[f'E{j}'] 
    text_cell.value = obj.Fenetre_type_2_Type_de_vitrage
    j+1
    text_cell = worksheet4[f'E{j}'] 
    text_cell.value = obj.Fenetre_type_2_Volets
    j+1
    text_cell = worksheet4[f'E{j}'] 
    text_cell.value = obj.Fenetre_type_2_Nombre
    for i in [obj.Fenetre_type_1_Materiaux,obj.Fenetre_type_1_Type_de_vitrage,
              obj.Fenetre_type_1_Volets,obj.Fenetre_type_1_Nombre]:
        
        #text_cell = worksheet4[f'E{j}'] 
        #text_cell.value = str(i)
        j+=1
        
    objimage =obj.Fenetre_type_1_Photo
    image_cell_1 = worksheet4['B160'] 
    image_cell_1.value = None
    if objimage:
        image_path_ =objimage.path  # Get the file path
        if default_storage.exists(image_path_):
            image_path1 = objimage.path
            img_1 = Image(image_path1)
            img_1.width =  185.28 #cell_width
            img_1.height = 140.16 # cell_height
            worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    
    ### Fenêtre 2
    j=169
    
    text_cell = worksheet4[f'B{j}'] 
    text_cell.value = f" {obj.Fenetre_type_1_Menuiserie}"
    j+=1
    for i in [obj.Fenetre_type_1_Materiaux,obj.Fenetre_type_2_Type_de_vitrage,
              obj.Fenetre_type_2_Volets,obj.Fenetre_type_2_Nombre]:
        
        #text_cell = worksheet4[f'E{j}'] 
        #text_cell.value = i
        j+=1
    
    
    
    
    objimage =obj.Fenetre_type_2_Photo
    image_cell_1 = worksheet4['B174'] 
    image_cell_1.value = None
    if objimage:
        image_path_ =objimage.path  # Get the file path
        if default_storage.exists(image_path_):
            image_path1 = objimage.path
            img_1 = Image(image_path1)
            img_1.width =  185.28 #cell_width
            img_1.height = 140.16 # cell_height
            worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    
    ### Porte 1
    j=183
    text_cell = worksheet4[f'E{j}'] 
    text_cell.value = obj.Porte_1_Materiaux
    j+=1
    text_cell = worksheet4[f'E{j}'] 
    text_cell.value = obj.Porte_1_Type_porte
    j+=1
    text_cell = worksheet4[f'E{j}'] 
    text_cell.value = obj.Porte_1_Nombre
    j+=1    
    objimage =obj.Porte_1_Photo_porte
    image_cell_1 = worksheet4['B186'] 
    image_cell_1.value = None
    if objimage:
        image_path_ =objimage.path  # Get the file path
        if default_storage.exists(image_path_):
            image_path1 = objimage.path
            img_1 = Image(image_path1)
            img_1.width =  185.28 #cell_width
            img_1.height = 140.16 # cell_height
            worksheet4.add_image(img_1, image_cell_1.coordinate)
            
            
    ### Porte 2
    j=195
    text_cell = worksheet4[f'E{j}'] 
    text_cell.value = obj.Porte_2_Materiaux
    j+=1
    text_cell = worksheet4[f'E{j}'] 
    text_cell.value = obj.Porte_2_Type_porte
    j+=1
    text_cell = worksheet4[f'E{j}'] 
    text_cell.value = obj.Porte_2_Nombre
    j+=1
    
    objimage =obj.Porte_2_Photo_porte
    image_cell_1 = worksheet4[f'B{j}'] 
    image_cell_1.value = None
    if objimage:
        image_path_ =objimage.path  # Get the file path
        if default_storage.exists(image_path_):
            image_path1 = objimage.path
            img_1 = Image(image_path1)
            img_1.width =  185.28 #cell_width
            img_1.height = 140.16 # cell_height
            worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    
    ### Cauffage 
    j=209
    text_cell = worksheet4[f'D{j}'] 
    text_cell.value = obj.Cauffage_systeme
    j+=1
    text_cell = worksheet4[f'D{j}'] 
    text_cell.value = 'obj.'
    j+=1
    text_cell = worksheet4[f'D{j}'] 
    text_cell.value = obj.Cauffage_annee_de_mise_en_oeuvre
    j+=1
    text_cell = worksheet4[f'D{j}'] 
    text_cell.value = "obj."
    j+=1
    text_cell = worksheet4[f'D{j}'] 
    text_cell.value = "obj."
    j+=1
    text_cell = worksheet4[f'D{j}'] 
    text_cell.value = obj.Cauffage_type_de_regulation
    j+=1
    
    #objimage =obj.
    #image_cell_1 = worksheet4[f'B{j}'] 
    #image_cell_1.value = None
    #if objimage:
    #    image_path_ =objimage.path  # Get the file path
    #    if default_storage.exists(image_path_):
    #        image_path1 = objimage.path
    #        img_1 = Image(image_path1)
    #        img_1.width =  185.28 #cell_width
    #        img_1.height = 140.16 # cell_height
    #        worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    
    ###  ECS
    j=236
    text_cell = worksheet4[f'D{j}'] 
    text_cell.value = obj.ECS_type
    j+=1
    
    objimage =obj.ECS_photo_appoint
    image_cell_1 = worksheet4[f'B{j}'] 
    image_cell_1.value = None
    if objimage:
        image_path_ =objimage.path  # Get the file path
        if default_storage.exists(image_path_):
            image_path1 = objimage.path
            img_1 = Image(image_path1)
            img_1.width =  185.28 #cell_width
            img_1.height = 140.16 # cell_height
            worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    text_cell = worksheet4[f'D{j}'] 
    text_cell.value = obj.ECS_system_d_appoint
    
    
    ###  Ventilation
    j=249
    text_cell = worksheet4[f'D{j}'] 
    text_cell.value = obj.Ventilation_type
    j+=1
    
    objimage =obj.Ventilation_photo_ventilation
    image_cell_1 = worksheet4[f'B{j}'] 
    image_cell_1.value = None
    if objimage:
        image_path_ =objimage.path  # Get the file path
        if default_storage.exists(image_path_):
            image_path1 = objimage.path
            img_1 = Image(image_path1)
            img_1.width =  185.28 #cell_width
            img_1.height = 140.16 # cell_height
            worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    
    ###  Refroidissement
    j=249
    text_cell = worksheet4[f'D{j}'] 
    text_cell.value = obj.Refroidissement_type
    j+=1
    
    #objimage =obj.Ventilation_photo_ventilation
    #image_cell_1 = worksheet4[f'B{j}'] 
    #image_cell_1.value = None
    #if objimage:
    #    image_path_ =objimage.path  # Get the file path
    #    if default_storage.exists(image_path_):
    #        image_path1 = objimage.path
    #        img_1 = Image(image_path1)
    #        img_1.width =  185.28 #cell_width
    #        img_1.height = 140.16 # cell_height
    #        worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    
    ###  Compteur Electrique
    j=269
    text_cell = worksheet4[f'D{j}'] 
    text_cell.value = obj.Compteur_Electrique_Puissance_souscrite
    j+=1
    text_cell = worksheet4[f'D{j}'] 
    text_cell.value = obj.Compteur_Electrique_type
    j+=1
    
    objimage =obj.Compteur_Electrique_photo_compteur
    image_cell_1 = worksheet4[f'B{j}'] 
    image_cell_1.value = None
    if objimage:
        image_path_ =objimage.path  # Get the file path
        if default_storage.exists(image_path_):
            image_path1 = objimage.path
            img_1 = Image(image_path1)
            img_1.width =  185.28 #cell_width
            img_1.height = 140.16 # cell_height
            worksheet4.add_image(img_1, image_cell_1.coordinate)
    
    
    

    ######################################   END WORK_SHEET_4
    ######################################   END WORK_SHEET_4
    ######################################   END WORK_SHEET_4
    
        ###################################################### save process #######################################################
    # Save the updated XLSX file temporarily
    # Generate the XLSX content as bytes
# Create a BytesIO object to store the XLSX content
    xlsx_content = BytesIO()

    # Save the workbook to the BytesIO object
    workbook.save(xlsx_content)

    # Seek to the beginning of the BytesIO object
    xlsx_content.seek(0)

    # Create an HttpResponse with the XLSX content for download
    response = HttpResponse(xlsx_content.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="Kizeo.xlsx"'

    return response