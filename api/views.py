from django.shortcuts import render
from mainapp.models import Tank
from rest_framework import views
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import TankSerializer
from .permissions import TankPermission

# class TankAPIView(views.APIView):
#     def get(self, request, pk):
#         tank = Tank.objects.get(pk=pk)
#         tank_ser = TankSerializer(tank)
#         return Response(data=tank_ser.data, status=status.HTTP_200_OK)

#     def delete(self, request, pk):
#         tank = Tank.objects.get(pk=pk)
#         tank.delete()
#         return Response(data={}, status=status.HTTP_200_OK)

#     def patch(self, request, pk):
#         tank = Tank.objects.get(pk=pk)
#         tank_ser = TankSerializer(tank, data=request.data)
#         if tank_ser.is_valid():
#             tank_ser.save()
#             return Response(data={}, status=status.HTTP_200_OK)
#         return Response(data=tank_ser.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, *args, **kwargs):
#         self.update(request, *args, **kwargs)


# class TankListAPIView(views.APIView):
#     def get(self, request):
#         tanks = Tank.objects.all()
#         tank_ser = TankSerializer(tanks, many=True)
#         return Response(data=tank_ser.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         tank_ser = TankSerializer(data=request.data)
#         if tank_ser.is_valid():
#             tank_ser.save()
#             return Response(data={}, status=status.HTTP_200_OK)
#         return Response(data=tank_ser.errors, status=status.HTTP_400_BAD_REQUEST)


class TankListAPIView(generics.ListCreateAPIView):
    queryset = Tank.objects.all()
    serializer_class = TankSerializer

    def get(self, request, *args, **kwargs):
        for key, value in request.session.keys():
            print(f'{key}: {value}')
        return super().get(request, *args, **kwargs)




class TankAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tank.objects.all()
    serializer_class = TankSerializer
    permission_classes = (TankPermission, )