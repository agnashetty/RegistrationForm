from django.shortcuts import render
from pyexpat import model
from django.shortcuts import render
from .models import customer
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.

class Registeration(View):
    def post(self, request):
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Registered Succesfully!')
            return redirect('/')

        return render(request, 'myapp/index.html', {'form':fm})
   
    def get(self, request):
        fm = RegistrationForm()
        return render(request, 'myapp/index.html', {'form':fm})
