from django.shortcuts import render



def home(request):
    return render(request, "home.html")


def autoren(request):
    return render(request, "autoren.html")





