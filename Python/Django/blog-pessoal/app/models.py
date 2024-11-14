from django.db import models
from django.contrib.auth.models import User

class Postagem(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.autor} - {self.titulo}'
    
# class Comentario(models.Model):
#     postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
#     autor = models.CharField(max_length=50)
#     conteudo = models.TextField()
#     data = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.autor} - {self.postagem.titulo}'
