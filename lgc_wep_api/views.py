
from lgc_wep_api.models import Users
from lgc_wep_api.serializers import UsersSerializer
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework import generics


@permission_classes((permissions.AllowAny,))
class UserList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


@permission_classes((permissions.AllowAny,))
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
