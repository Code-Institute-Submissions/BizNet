from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
# from .models import User

from .models import Profileuser, Industry

# Create your views here.

def profile(request):
    # profiles = Profileusers.objects.all()
    # context = {
    #    'profiles': profiles
    # }
    return render(request, 'profileusers/profile.html')
