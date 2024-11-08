from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Ator(models.Model):
    nome = models.CharField(max_length=150)
    nacionalidade = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    idade = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nome

class Diretor(models.Model):
    nome = models.CharField(max_length=150)
    nacionalidade = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    idade = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nome
    
class ProdutorSerie(models.Model):
    nome = models.CharField(max_length=150)
    nacionalidade = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    idade = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nome

class Poster(models.Model):
    foto = models.ImageField(upload_to='posters/')
    
    def __str__(self):
        return str(self.foto)

class Genero(models.Model):
    nome = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nome
class Producao(models.Model):
    nome = models.CharField(max_length=150)
    poster = models.OneToOneField(Poster, on_delete=models.CASCADE, related_name='filme', blank=True, null=True)
    data_lancamento = models.DateField()
    diretor = models.ManyToManyField(Diretor, related_name='filmes_dirigidos')
    elenco = models.ManyToManyField(Ator, related_name='filmes_participados')
    genero = models.ManyToManyField(Genero, related_name='filmes_genero')
    tipo_choices = [ ('FILME', 'Filme'), ('SERIE', 'Série') ]
    tipo = models.CharField(max_length=5, choices=tipo_choices)
    nome_original = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nome

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    producoes_favoritas = models.ManyToManyField(Producao, related_name='series_favoritas')    
    
    def __str__(self):
        return self.user.username

class Comentario(models.Model):
    autor = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    Producao = models.ForeignKey(Producao, on_delete=models.CASCADE, related_name='comentarios', blank=True, null=True)    
    
    def __str__(self):
        return f'Comentário de {self.autor} em {self.data}'

    def clean(self):
        if not self.serie and not self.filme:
            raise ValidationError('O comentário deve estar associado a um filme ou uma série.')
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
