from django.shortcuts import render
from todoHandling.models import TODO


def home(request):
    todos = TODO.objects.all()
    args = {'todos': todos}
    return render(request, "home.html", args)


def autoren(request):
    return render(request, "autoren.html")





