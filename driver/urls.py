from django.urls import path
from .views import DriverView,DriverId

urlpatterns=[
    path('getall/',DriverView.as_view()),
    path('mod/<int:id>',DriverId.as_view())
]