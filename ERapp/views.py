from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.models import User

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login , logout

from .forms import TableDataForm1
from .models import TableData1


from django.core.mail import send_mail
# Create your views here.


def Home(request):
    send_mail(
    "Subject here",
    "Here is the message. test test 123 ",
    "lazariatik@gmail.com",
    ["belaatiknizar@gmail.com"],
    fail_silently=False,
)
    
    #return render(request,'html/home.html',{"name":"night","username":"nightcode"})
    return render(request,'html/home.html')
    



def LoginU(request):
    
    
    if request.method == "POST":
        
        usernameU =request.POST.get('username')
        passwordU =request.POST.get('password')
        
        user = authenticate(username=usernameU,password=passwordU)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/home') 

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
    
    

def table_view(request):
    if request.method == 'POST':
        form = TableDataForm1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/formT/')  # Redirect to the same page to add more rows
    else:
        form = TableDataForm1()
    data = TableData1.objects.all()
    return render(request, 'html/formPage.html', {'form': form, 'data': data})