
from lgc_wep_api.models import Users
from lgc_wep_api.serializers import UsersSerializer
from rest_framework import permissions
from rest_framework import generics


class UserList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
