from skapp.models import User
from skapp.Api.serializers import Userserializers
from rest_framework import viewsets

class Userview(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class= Userserializers