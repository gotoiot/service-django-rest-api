from rest_framework import permissions


class IsInstanceOwner(permissions.BasePermission):
    """
    Permission to determine if current user is the instance taker
    """
    def has_object_permission(self, request, view, assesment_instance):
        return assesment_instance.taker.user == request.user