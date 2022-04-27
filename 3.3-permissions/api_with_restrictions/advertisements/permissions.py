from rest_framework import permissions


class IsAdminOrOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if (request.user.is_superuser) or (request.method in permissions.SAFE_METHODS) :
            return True

        return obj.creator == request.user
