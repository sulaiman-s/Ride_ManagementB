from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.response import Response
# Create your views here.
from .models import Notify


class NotifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Notify
        fields = ['id', 'username', 'expotoken']


class NotifyView(APIView):
    def get(self, request):
        get_all_tokens = Notify.objects.all()
        serialize = NotifySerializer(get_all_tokens, many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = NotifySerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response("data sent successfuly")
