from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    debito = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.usuario.username

class Patinete(models.Model):
    TIPOS_CHOICES = [
        ('Tipo 1', 'Tipo 1'),
        ('Tipo 2', 'Tipo 2'),
        ('Tipo 3', 'Tipo 3'),
        # Agrega más tipos según sea necesario
    ]

    numero = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50, choices=TIPOS_CHOICES)
    precio_desbloqueo = models.DecimalField(max_digits=10, decimal_places=2)
    precio_minuto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.numero

class Alquiler(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    patinete = models.ForeignKey(Patinete, on_delete=models.CASCADE)
    fecha_desbloqueo = models.DateTimeField()
    fecha_entrega = models.DateTimeField()
    coste_final = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.usuario.usuario.username} alquiló {self.patinete.numero}"