from socket import setdefaulttimeout
from django.urls import path
from .views import PersonDriverView, PersonDriverId, set_msg, set_driver_Location

urlpatterns = [
    path('getall/', PersonDriverView.as_view()),
    path('mod/<int:id>', PersonDriverId.as_view()),
    path('mod/driver/<name>', set_msg),
    path('mod/loc/<name>', set_driver_Location)
]
