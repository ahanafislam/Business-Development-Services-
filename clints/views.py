from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from account.models import ServiceProviderList
from .forms import Submit_document_form
from .models import Submit_document
from django.contrib.auth.models import User
from serviceProvider.models import Provider_submit


@login_required
def user_home(request):
    form = Submit_document_form(request.POST,request.FILES)
    if form.is_valid():
        form.instance.submitor = request.user
        form.save()
    return render(request,'clints/user_home.html',{"form":form})

@login_required
def notification(request):
    notification = Provider_submit.objects.all()
    return render(request,'clints/notification.html',{"notification":notification})

@login_required
def nDetails(request,provider_id):
        view_doc = get_object_or_404(Provider_submit,pk = provider_id)
        return render(request,'clints/nDetails.html',{"notification":view_doc})

@login_required
def submited(request):
    submited = Submit_document.objects.all()
    return render(request,'clints/submited.html',{"submited":submited})

@login_required
def subDetail(request,company_id):
        view_doc = get_object_or_404(Submit_document,pk = company_id)
        return render(request,'clints/subDetail.html',{"submited":view_doc})
