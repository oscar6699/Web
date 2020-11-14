from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

# Create your models here.

fs = FileSystemStorage(location='/media/photos')
class Plan(models.Model):
    NombrePlan = models.CharField(max_length=30)
    descripcion = models.TextField();
    precio = models.IntegerField();
    fecha = models.DateTimeField(default=timezone.now);
    imagen = models.ImageField(upload_to="planes", null = True)
    
    def __str__(self):
        return self.NombrePlan
    
class Plan_Contratado(models.Model):
    idUser = models.ForeignKey('auth.User', on_delete=models.CASCADE);
    idPlan = models.ForeignKey('Plan', on_delete=models.CASCADE);
    fechaPlan = models.DateTimeField(default=timezone.now);
    
    def __str__(self):
        return self.fechaPlan