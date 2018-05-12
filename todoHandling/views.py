from django.shortcuts import render
from .models import TODO
from .forms import TodoForm
from django.views.generic.edit import UpdateView


# Create your views here.
def create(request):
    return render(request, 'todo_form.html')


class todo_Update(UpdateView):
    model = TODO
    fields = ['title', 'description', 'deadline', 'progress', ]

def todo_create(request):
    form = TodoForm(request.POST or None)
    print(form)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
        "form": form,
    }

    return render(request, "todo_form.html", context)
