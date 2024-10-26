from django.db import models

# Creamos un modelo(tabla) que representa a la categoria de los productos
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

# creamos el modelo para cada uno de los productos 
class productos(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='Productos',blank=True)
    
    def __str__(self):
        return self.nombre 