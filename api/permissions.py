import re
from rest_framework import permissions


class TankPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        token = request.query_params.get('token')
        return bool(
            token and 
            token == '123'
        )


    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS:
            return bool(not obj.premium)
        return True