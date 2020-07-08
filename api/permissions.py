from rest_framework.response import Response
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.status import HTTP_400_BAD_REQUEST

from django.shortcuts import get_object_or_404

from .models import Follow, User


class IsOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if hasattr(obj, 'user'):
            return request.user == obj.user
        return request.user == obj.author
