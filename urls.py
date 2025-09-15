from django.urls import path
from . import views

urlpatterns = [
    path('', views.alerts_contacts, name='alerts_contacts'),
]