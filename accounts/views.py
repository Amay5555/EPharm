from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user) 
            return redirect('home')    
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


