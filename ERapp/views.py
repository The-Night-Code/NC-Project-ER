from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.models import User

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login , logout

from django.views.generic.edit import CreateView


from .models import ImageModel,USER,TableData001,file_table_auditV1,file_table_auditV2,file_table_auditV3,file_table_vt,file_table_auditFinal,message_box_1


from django.core.mail import send_mail
# Create your views here.
import random
import string


import openpyxl
from openpyxl.utils import get_column_letter
from openpyxl.drawing.image import Image
from django.http import HttpResponse
from .models import MyModel, UpdatedXLSXFile 



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
    user_Id="3"
    user_L=USER.objects.get(user_id=user_Id) 
    
    Submit_Upload_image=request.POST.get("Submit_Upload_image")
    remove_profile_image=request.POST.get("remove_profile_image")
    
    # Upload Profile Image
    if request.method == 'POST' :
        user_L = USER.objects.get(user_id=user_Id)
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
    update_xlsx_template(request)
    
    
    
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
    for i in range(2,17):
        ws1[f"B{i}"].value ="night code"
    
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
            image_path = obj.image_field.path
            
            
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