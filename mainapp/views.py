from django.shortcuts import render, redirect
from .models import Tank, TankProperties
from .forms import TankForm, TankPropertiesForm
from django.views import View
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse 
from django.template.loader import get_template
from .tasks import add
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    print(request.user)
    request.session['key'] = 42
    for key, value in request.session.items():
        print(f'{key}: {value}')
    return HttpResponse('hello')


def index2(request):
    tanks = Tank.objects.all()
    return TemplateResponse(request, 'mainapp/index.html', {'tanks': tanks})


class CreateTankView2(View):
    def get(self, request):
        return render(request, 'mainapp/create_tank2.html')

    def post(self, request):
        name = request.POST['name']
        lvl = request.POST['lvl']
        premium = True if request.POST.get('premium') else False
        tank = Tank(name=name, lvl=lvl, premium=premium)
        errors = None
        try:
            tank.full_clean()
        except ValidationError as e:
            errors = e.message_dict
        if errors:
            return render(request, 'mainapp/create_tank2.html',
                          context={
                              'tank': tank,
                              'errors': errors,
                          })
        tank.save()
        return redirect('index')


class CreateTank(View):
    def get(self, request):
        form = TankForm()
        return render(request, 'mainapp/create_tank.html', context={'form': form})

    def post(self, request):
        form = TankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'mainapp/create_tank.html', context={'form': form})



class CreateTankPropertiesView(View):
    def get(self, request):
        form = TankPropertiesForm()
        for_tank = request.GET.get('for_tank')
        if for_tank:
            form.fields['tank'].initial = int(for_tank)
        return render(request, 'mainapp/create_tank_properties.html', context={'form': form})

    def post(self, request):
        form = TankPropertiesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'mainapp/create_tank_properties.html', context={'form': form})

# @api_view(['GET'])
# def api_tank_get(request, pk):
#     tank = get_object_or_404(Tank, pk=pk)
#     tank_ser = TankSerializer(tank)
#     return Response(tank_ser.data)

# @api_view(['POST'])
# def api_tank_create(request):
#     tank_ser = TankSerializer(data=request.POST)
#     if tank_ser.is_valid():
#         tank_ser.save()
#         return Response(tank_ser.data, status=status.HTTP_201_CREATED)
#     return Response(tank_ser.data, status=status.HTTP_400_BAD_REQUEST)


class TankRetriveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Tank.objects.all()
    serializer_class = TankSerializer

class TankListAPIView(ListAPIView):
    queryset = Tank.objects.all()
    serializer_class = TankListSerializer

    def get(self, request, *args, **kwargs):
        print(request.user.username)
        res = self.list(request, *args, **kwargs)