import random

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Permission
from django_filters.rest_framework import DjangoFilterBackend
import string
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from main.serializers.user_ser import UserSerializer


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id"]
    authentication_classes = []

    @action(['get'], False, 'all-permissions')
    def get_all_permissions(self, request):
        permissions = Permission.objects.all()

        return Response([{"codename": p.codename, "name": p.name} for p in permissions if "can_view_" in p.codename])

    @action(['get'], detail=True, url_path='reset-pass')
    def reset_pass(self, request, pk):
        new_password = get_random_string(6)
        instance = self.get_object()
        instance.password = make_password(str(new_password))
        instance.save()
        return Response({"password": new_password})

    @action(['patch'], detail=True, url_path='update-pass')
    def update_pass(self, request, pk):
        new_password = request.data["new_password"]
        instance = self.get_object()
        instance.password = make_password(str(new_password))
        instance.save()
        return Response({"password": new_password})


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
