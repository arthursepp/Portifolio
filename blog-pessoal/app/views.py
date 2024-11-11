from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def index(request):
    postagem = Postagem.objects.all()
    return render(request, 'index.html', {'postagem': postagem})

@login_required
def home(request):
    postagem = Postagem.objects.all()
    return render(request, 'home.html', {'postagem': postagem})

@login_required
def novo_post(request):
    if request.method == 'POST':
        form = PostagemForm(request.POST)
        if form.is_valid():
            postagem = form.save(commit=False)
            postagem.autor = request.user
            postagem.save()
            return redirect('home')
    else:
        form = PostagemForm()
    return render(request, 'novo_post.html', {'form': form})

