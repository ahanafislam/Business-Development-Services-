from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from clints.models import Submit_document
from django.contrib.auth.models import User
from .models import Provider_submit
from .forms import Provider_submit_form

@login_required
def svProvider_home(request):
    view_doc = Submit_document.objects.all()
    return render(request,'serviceProvider/svProvider_home.html',{"view_doc":view_doc})

@login_required
def svDetails(request,company_id):
    view_doc = get_object_or_404(Submit_document,pk = company_id)
    form = Provider_submit_form(request.POST,request.FILES)
    if form.is_valid():
        form.instance.feedbackFor = request.user
        form.save()
        return render(request,'serviceProvider/svDetails.html',{"view_doc":view_doc,"form":form})
    else:
        return render(request,'serviceProvider/svDetails.html',{"view_doc":view_doc,"form":form})
