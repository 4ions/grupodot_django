from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.

from rest_framework import viewsets
from .serializers import InfoUserSerializer
from .models import InfoUser
import json

class InfoUserViewSet(viewsets.ModelViewSet):
    queryset = InfoUser.objects.all().order_by('socio')
    serializer_class = InfoUserSerializer

    
    def list(self, request):
        queryset = InfoUser.objects.all()
        serializer = InfoUserSerializer(queryset, many=True)
        print(queryset)
        return Response(serializer.data)


    def create(self, request):
        if (len(request.data) != 1):
            return Response({"error": "solo debe especificar el monto del prestamo"})

        try:
            print(request.data['monto'])
        except:
            return Response({"error": "solo debe especificar el monto del prestamo", "ejemplo": "monto:valor"})

        if (type(request.data['monto']) == int):
            
            info = InfoUser.objects.order_by('tasa').filter(mon_max__gte=request.data['monto'])
            if info:
                vf = int(request.data['monto'])*(1 + (36) * (info[0].tasa/100)) 
                ct = vf / 36
                return Response({
                    "Socio que realiza el prestamo": info[0].socio,
                    "Cuota Mensual": round(ct,2),
                    "Pago total del credito": round(vf,2),
                    "Tasa de interés mensual": info[0].tasa
                })

            else:
                return Response({"msg": "No hay socio disponible"})
    
        return Response({"error": "Algo extraño ha pasado"})