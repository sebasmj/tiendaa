from django.db import models

class Mensaje(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100, default='')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    cantidad = models.IntegerField(default=0)
    mensaje = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre