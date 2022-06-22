from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from .models import Driver


# Create your views here.

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'username', 'password', 'email', 'driver_liscence_pic', 'is_registered', 'available_seats',
                  'pickup_Location', 'drop_Location', 'vehicle_no', 'ph_no', 'police_record', 'is_airConditioned']


class DriverView(APIView):
    def get(self, request):
        get_all_Driver = Driver.objects.all()
        serialize = DriverSerializer(get_all_Driver, many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = DriverSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response("data sent successfuly")


class DriverId(APIView):
    def patch(self, request, id):
        driver_to_update = Driver.objects.get(pk=id)
        pf_s = DriverSerializer(
            driver_to_update, data=request.data, partial=True)
        pf_s.is_valid(raise_exception=True)
        pf_s.save()
        return Response(pf_s.data)

    def delete(self, request, id):
        driver_to_delete = Driver.objects.get(pk=id)
        driver_to_delete.delete()
        return Response("data deleted successfully")
