from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm # Django Default

def register(request):
    
    form = UserCreationForm()

    return render(request, 'users/register.html', {'form':form})
