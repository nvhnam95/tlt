from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Permission
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "user_permissions"]

    def to_representation(self, instance):
        re = super().to_representation(instance)
        permissions = instance.user_permissions.all()
        re["user_permissions"] = [p.codename for p in permissions if "can_view_" in p.codename]
        return re

    def create(self, validated_data):
        raw_pass = self.initial_data["password"]
        validated_data["password"] = make_password(raw_pass)
        instance = super().create(validated_data)
        for p in self.initial_data.get("permissions", []):
            try:
                permission = Permission.objects.get(codename=p)
                instance.user_permissions.add(permission)
            except Permission.DoesNotExist:
                raise Exception("permission not found")
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)

        if "permissions" in self.initial_data:
            instance.user_permissions.clear()
        for p in self.initial_data["permissions"]:
            try:
                permission = Permission.objects.get(codename=p)
                instance.user_permissions.add(permission)
            except Permission.DoesNotExist:
                raise Exception("permission not found")

        return instance
