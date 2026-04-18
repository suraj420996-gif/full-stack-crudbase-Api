from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm
from .models import User


# Create your views here.
def add_show(request):
    if request.method == 'POST':
      form = UserForm(request.POST)
      if form.is_valid():
            form.save()
    else:
       form = UserForm()
    User_data = User.objects.all()
    return render(request,'enroll/add_and_show.html', {'form':form, 'User_data':User_data})
def Delet_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')


def update_data(request, id):
    pi = User.objects.get(pk=id)

    if request.method == "POST":
        form = UserForm(request.POST, instance=pi)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = UserForm(instance=pi)

    return render(request, 'enroll/update.html', {'form': form})