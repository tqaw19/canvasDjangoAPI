from django.db import models

# Create your models here.
class Curso (models.Model):

    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100)
    dni=models.CharField(max_length=100)
    
    class Meta:
        db_table = "cursos"
        
    def __str__(self):
        return self.nombre
        
     
