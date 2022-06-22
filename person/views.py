from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.response import Response
from .models import PersonDriver


# Create your views here.

class PersonDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonDriver
        fields = ['id', 'driver_name', 'person_name', 'seats_booked', 'message',
                  'person_address', 'person_pickup_Time', 'driver_location', 'person_location']


class PersonDriverView(APIView):
    def get(self, request):
        get_all_booked = PersonDriver.objects.all()
        serialize = PersonDriverSerializer(get_all_booked, many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = PersonDriverSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response("data sent successfuly")


class PersonDriverId(APIView):

    def patch(self, request, id):
        booked_to_update = PersonDriver.objects.get(pk=id)
        pf_s = PersonDriverSerializer(
            booked_to_update, data=request.data, partial=True)
        pf_s.is_valid(raise_exception=True)
        pf_s.save()
        return Response(pf_s.data)

    def get(self, request, id):
        get_booked = PersonDriver.objects.get(pk=id)
        serialize = PersonDriverSerializer(get_booked)
        return Response(serialize.data)

    def delete(self, request, id):
        booked_to_delete = PersonDriver.objects.get(pk=id)
        booked_to_delete.delete()
        return Response("data deleted successfully")


@api_view(['POST'])
def set_msg(request, name):
    message = request.data['message']
    PersonDriver.objects.filter(
        driver_name__exact=name).update(message=message)
    return Response("message sent")


@api_view(['POST'])
def set_driver_Location(request, name):
    driver_loc = request.data['location']
    PersonDriver.objects.filter(driver_name__exact=name).update(
        driver_location=driver_loc)
    return Response("updated")
