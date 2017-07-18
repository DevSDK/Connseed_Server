from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from Web.fomrs import LoginForm


def MainPage(request):
    if not request.user.is_authenticated():
        return redirect('/account')

    return render(request, "connseed/index.html")

def Profile(request):
    if not request.user.is_authenticated():
        return redirect('/account')
    return render(request, "connseed/profile.html")

def Account(request):
    if request.method == 'GET':
        form = LoginForm()
        context = { 'form' : form}
        return render(request, "connseed/account.html", context)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if(form.is_valid()):
            user = auth.authenticate(username = form.cleaned_data['id'], password = form.cleaned_data['password'])
            if user is None:
                return render(request, "connseed/account.html", {'form':form})
            if user.is_active:
                auth.login(request,user)
                return redirect('/')
            return HttpResponse('isLogin')
    return render(request, "connseed/account.html", {'form': form})

def Device(request):
    if not request.user.is_authenticated():
        return redirect('/account')

    return render(request, "connseed/device.html")

def Monitoring(request):
    if not request.user.is_authenticated():
        return redirect('/account')


    return render(request, "connseed/monitoring.html")

def Analysis(request):
    if not request.user.is_authenticated():
        return redirect('/account')


    return render(request, "connseed/analysis.html")


def TestReq(request):
    return render(request, "connseed/test.html")
