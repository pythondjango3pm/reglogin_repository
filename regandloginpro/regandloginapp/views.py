from django.shortcuts import render
from .forms import RegistrationForm,LoginForm
from .models import RegistrationData
from django.http.response import HttpResponse

def reg_view(request):
    if request.method =="POST":
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            first_name = request.POST.get('first_name','')
            last_name = request.POST.get('last_name','')
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            mobile = request.POST.get('mobile','')
            email = request.POST.get('email','')

            data = RegistrationData(first_name=first_name,last_name=last_name,
                   username=username, password=password, mobile=mobile,email=email )
            data.save()
            lform = LoginForm()
            return render(request, 'login_form.html', {'lform': lform})
        else:
            return HttpResponse("Invalid Data")
    else:
        rform = RegistrationForm()
        return render(request,'reg_form.html',{'rform':rform})


def login_view(request):
    if request.method =="POST":
        lform = LoginForm(request.POST)
        if lform.is_valid():
            uname = request.POST.get('username','')
            pwd = request.POST.get('password','')
            uname1 = RegistrationData.objects.filter(username=uname)
            pwd1 = RegistrationData.objects.filter(password=pwd)
            if uname1 and pwd1:
                return render(request,'thankyou.html')
                # return HttpResponse("Correct Username and password")
            else:
                return HttpResponse("Wrong username or password")
        else:
            return HttpResponse("Invalid Deta")
    else:
        lform = LoginForm()
        return render(request,'login_form.html',{'lform':lform})
