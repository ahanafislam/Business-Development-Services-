from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import ServiceProviderList
from .models import CompanyDetails

def home(request):
    if request.method =="POST":
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            user_name = User.objects.get(username=request.POST["username"])
            try:
                provider_list = ServiceProviderList.objects.get(provider__username=user_name)
                return redirect("svProvider_home")
            except ServiceProviderList.DoesNotExist:
                return redirect("user_home")
        else:
            return render(request,'account/home.html',{"error":"The Username Or Password Is Incorrect ."})
    else:
        return render(request,'account/home.html')


def signup(request):
        if request.method == "POST":
            if request.POST['password1']==request.POST['password2']:
                try:
                    user=User.objects.get(username=request.POST['username1'])
                    return render(request,'account/signup.html',{'error':'This Username Is Alrady Exist'})
                except User.DoesNotExist:
                    user = User.objects.create_user(request.POST['username1'],password=request.POST['password1'],first_name=request.POST['firstName'],last_name=request.POST['lastName'],email=request.POST['email'])
                    auth.login(request,user)
                    return redirect('companyDetails')
            else:
                return render(request,'account/signup.html',{"error":"Password not match"})
        else:
            return render(request,'account/signup.html')


def companyDetails(request):
    if request.method == "POST":
        if request.POST['company'] and request.POST['country']:
            companyDetails = CompanyDetails()
            companyDetails.company_name = request.POST['company']
            companyDetails.logo = request.FILES['logo']
            if request.POST['website'].startswith('http://') or request.POST['website'].startswith('https://'):
                companyDetails.website = request.POST['website']
            else:
                companyDetails.website = 'http://' + request.POST['website']
            companyDetails.street_address = request.POST['street_address']
            companyDetails.city = request.POST['city']
            companyDetails.state = request.POST['state']
            companyDetails.zip_code = request.POST['zip_code']
            companyDetails.country = request.POST['country']
            companyDetails.company = request.POST['company']
            companyDetails.user = request.user
            companyDetails.save()
            return redirect('user_home')
        else:
            return render(request,'account/companyDetails.html')
    else:
        return render(request,'account/companyDetails.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
