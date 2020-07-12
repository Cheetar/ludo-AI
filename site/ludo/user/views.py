from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import User

def index(request):
    return render(request, 'user/index.html')

def name(request, user_id):
    response = "Ten użytkownik ma na imię:  %s."
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user/profile.html', {'title':user.title})
