from django.db import models

class Zona(models.Model):
    nombre_zona = models.CharField(max_length=100)
    tarifa_por_kg = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_zona
    
class Repartidor(models.Model):
    nombre_repartidor = models.CharField(max_length=100)
    email_repartidor = models.EmailField(blank=True, null=True)  

    def __str__(self):
        return self.nombre_repartidor
    
class Envio(models.Model):
    peso_kg = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_envio = models.DateField()
    zona_destino = models.ForeignKey(Zona, on_delete=models.CASCADE)
    repartidor_asignado = models.ForeignKey(Repartidor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Envio de {self.peso_kg} kg a {self.zona_destino.nombre_zona} por {self.repartidor_asignado.nombre_repartidor}"