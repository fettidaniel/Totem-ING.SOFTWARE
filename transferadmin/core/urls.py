from django.urls import path
from .views import home, datos, realizado, transfer
urlpatterns=[
    path('', home, name="home"),
    path('datos/', datos, name="datos"),
    path('realizado/', realizado, name="realizado"),
    path('transfer/', transfer, name="transfer"),
]