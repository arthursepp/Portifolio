from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    return render(request, 'index.html')

@login_required
def home(request):
    filmes = Filme.objects.all()
    return render(request, 'home.html', {'filmes': filmes})
