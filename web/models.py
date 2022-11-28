from django.contrib.auth.models import User,AbstractUser
from django.db import models

class User(AbstractUser):
    identificacion=models.CharField(max_length=100, blank=True, default='')
    telefono=models.CharField(max_length=50, null=True)
    pais=models.CharField(max_length=50, blank=True, default='')
    departamento=models.CharField(max_length=50, blank=True, default='')
    ciudad=models.CharField(max_length=50, blank=True, default='')
    direccion=models.CharField(max_length=100, blank=True, default='')

# Create your models here.
class Car(models.Model):
    foto = models.FileField(null=True)
    marca = models.CharField(max_length=50, null=True)
    modelo = models.CharField(max_length=50, null=True)
    anio = models.CharField(max_length=50,null=True)
    combustible = models.CharField(max_length=50, null=True)
    puertas = models.IntegerField(null=True)
    transmision = models.CharField(max_length=50, null=True)
    motor =models.FloatField(null=True)
    potencia =models.CharField(max_length=50, null=True)
    tipo =models.CharField(max_length=50, null=True)
    consumo = models.FloatField(null=True)
    estado = models.CharField(max_length=50, null=True)
    kilometros =models.IntegerField(null=True)
    pais =models.CharField(max_length=50, null=True)
    descripcion = models.TextField()
    precio = models.FloatField(null=True)
    anadido_por = models.ForeignKey(User, on_delete=None, null=True)

    def __str__(self):
        return self.marca + " " + self.modelo


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    address = models.TextField()
    approved_by = models.ForeignKey(User, on_delete=None, null=True, related_name='approved_by_user')
    is_delivered = models.BooleanField(default=False)
    nombre=models.CharField(max_length=100, null=True)
    identificacion=models.CharField(max_length=100, null=True)
    pais=models.CharField(max_length=50, null=True)
    departamento=models.CharField(max_length=50, null=True)
    ciudad=models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' - ' + self.car.modelo
