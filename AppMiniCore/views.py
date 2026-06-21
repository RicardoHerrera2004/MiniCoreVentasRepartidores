from django.shortcuts import render
from django.db.models import Sum, Count, F
from .models import Repartidor

def reporte_costos(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    
    repartidores = None
    error_fecha = None
    
    if fecha_inicio and fecha_fin:
        if fecha_inicio > fecha_fin:
            error_fecha = "La fecha de inicio no puede ser mayor que la fecha de fin."
        else: 
            repartidores = Repartidor.objects.filter(
                envio__fecha_envio__range=[fecha_inicio, fecha_fin]            
            ).annotate(
                total_envios=Count('envio'),
                total_kg=Sum('envio__peso_kg'),
                costo_total=Sum(F('envio__peso_kg') * F('envio__zona_destino__tarifa_por_kg'))
            ).distinct(
            ).order_by('-costo_total')
            
            for repeticion in repartidores:
                
                zonas = repeticion.envio_set.filter(
                    fecha_envio__range=[fecha_inicio, fecha_fin]
                ).values_list('zona_destino__nombre_zona', flat=True).distinct()
                
                tarifas = repeticion.envio_set.filter(
                    fecha_envio__range=[fecha_inicio, fecha_fin]
                ).values_list('zona_destino__tarifa_por_kg', flat=True).distinct()
                
                repeticion.zonas = ", ".join(str(z) for z in zonas)
                repeticion.tarifas = ", ".join([f"${tarifa:.2f}" for tarifa in tarifas])
    
    context = {
        'repartidores': repartidores,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin, 
        'error_fecha': error_fecha
    }
    return render(request, 'reporte_costos.html', context)
