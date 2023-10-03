from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.models import User

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login , logout

from django.views.generic.edit import CreateView

from .forms import TableDataForm1,ImageForm
from .models import TableData1,ImageModel,USER,TableData001,file_table_auditV1,file_table_auditV2,file_table_auditV3,file_table_vt


from django.core.mail import send_mail
# Create your views here.
import random
import string


formT="/formT/"


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
            return HttpResponseRedirect('/formT') 

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
        #if request.FILES['cell_data5add']:
        cell_id = generate_random_string(10)
        
        firstname = request.POST.get("cell_data1add")
        lastname = request.POST.get("cell_data2add")
        address = request.POST.get("cell_data3add")
        num = request.POST.get("cell_data4add")
        vt1 = request.FILES.getlist('cell_data5add')
        etat = request.POST.get("cell_data6add")
        #tp = request.POST.get("cell_data7")
        #auditV1 = request.FILES["cell_data8"]
        #auditV2 = request.FILES["cell_data9"]
        #auditV3 = request.FILES["cell_data10"]
        #coffrac = request.POST.get("cell_data11")
        
        up_files = ""; 
        #for uploaded_file in vt:
            #up_files+=uploaded_file + " "
        #form = TableDataForm1(request.POST)
        #if firstname or lastname or address or num and etat:
        #data = TableData001(cell_id=cell_id ,firstname=firstname ,lastname=lastname ,address=address ,num=num ,vt=vt ,etat=etat ,tp=tp ,auditV1=auditV1 ,auditV2=auditV2 ,auditV3=auditV3 ,coffrac=coffrac)
        for uploaded_file in vt1:
            TableData001.objects.create(
                cell_id=cell_id, 
                firstname=firstname, 
                lastname=lastname, 
                address=address, 
                num=num, 
                vt=uploaded_file, 
                etat=etat  
            )
            
        #data = TableData001(cell_id=cell_id ,firstname=firstname ,lastname=lastname ,address=address ,num=num , vt=up_files  ,etat=etat )
        
        #data = TableData001(cell_data=cell_data1,cell_data2=cell_data2)
        
        #data.save()
        return redirect('/formT/')
    
    

    data = TableData001.objects.all()
    datafiles = file_table_auditV1.objects.all()
    col_count = data.count()
    # Get unique column names from the TableData model
    column_names = TableData001._meta.get_fields()
    
    return render(request, 'html/formPage.html', { 'data': data ,'datafiles': datafiles , 'col_count':col_count ,'column_names': column_names})
       
    
    

    
def table_view_edit(request):
    
    param_value_id = request.GET.get('param0')
    param1_value = request.GET.get('param1')
    param2_value = request.GET.get('param2')
    param3_value = request.GET.get('param3')
    param4_value = request.GET.get('param4')
    param5_value = request.FILES.getlist('param5')
    param6_value = request.GET.get('param6')
    
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
        get_col_by_id.vt = param5_value
        get_col_by_id.etat = param6_value
        #get_col_by_id.save(update_fields=['firstname', 'lastname','address','num','vt','etat'])
        get_col_by_id.save(update_fields=['firstname', 'lastname','address','num','etat'])
    return redirect('/formT/')
     
    





    

    data = TableData001.objects.all()
    col_count = data.count()
    # Get unique column names from the TableData model
    column_names = TableData001._meta.get_fields()
    
    return render(request, 'html/test.html', { 'data': data , 'col_count':col_count ,'column_names': column_names})
       
    
    

    



def remove_file_from_auditV1(request):
    
    file_id = request.GET.get('param0')
    index = request.GET.get('param1')
    try:
        f_table_audit_v1 =file_table_auditV1.objects.get(file_id=str(file_id),file_index=str(index))
    except file_table_auditV1.DoesNotExist:
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
