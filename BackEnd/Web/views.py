from django.shortcuts import render

# Create your views here.

def MainPage(request):
    return render(request, "conseed/index.html")

def Account(request):
    return render(request, "conseed/account.html")

def Device(request):
    return render(request, "conseed/device.html")

def Monitoring(request):
    return render(request, "conseed/monitoring.html")

def Analysis(request):
    return render(request, "conseed/analysis.html")

