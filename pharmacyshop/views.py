from django.shortcuts import render,redirect
from store.models import Meds
def home(request):
    meds = Meds.objects.filter(qty__gte = 1)
    context = {
        'meds' : meds
    }
    return render(request, 'home.html', context)

