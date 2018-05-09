from django.shortcuts import render
from .models import TODO
from django.views.generic.edit import CreateView


# Create your views here.
def create(request):
    return render(request, 'todoHandling/todo_form.html')


class ObjectCreate(CreateView):
    print('hello World')
    model = TODO
    fields = ['title', 'description', 'deadline', 'progress']
