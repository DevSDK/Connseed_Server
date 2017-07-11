from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from Web.fomrs import LoginForm


def MainPage(request):
    return render(request, "conseed/index.html")

def Account(request):
    if request.method == 'GET':

        if request.user.is_authenticated():
            return redirect('/')
        form = LoginForm()
        context = { 'form' : form}
        return render(request, "conseed/account.html",context)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if(form.is_valid()):
            user = auth.authenticate(username = form.cleaned_data['id'], password = form.cleaned_data['password'])
            if user is None:
                return render(request, "conseed/account.html", { 'form':form })
            if user.is_active:
                auth.login(request,user)
                return redirect('/')
            return HttpResponse('isLogin')


def Device(request):
    if not request.user.is_authenticated():
        return redirect('/account')

    return render(request, "conseed/device.html")

def Monitoring(request):
    if not request.user.is_authenticated():
        return redirect('/account')


    return render(request, "conseed/monitoring.html")

def Analysis(request):
    if not request.user.is_authenticated():
        return redirect('/account')


    return render(request, "conseed/analysis.html")

