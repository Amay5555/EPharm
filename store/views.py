from django.shortcuts import render, get_object_or_404
from . import models

def prodInfo(request , pk):
    med = get_object_or_404 (models.Meds , pk = pk)
    context = {
        med : 'med'
    }
    return render(request , 'prod_details.html', context )



