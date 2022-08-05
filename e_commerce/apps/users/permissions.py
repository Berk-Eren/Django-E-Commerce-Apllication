from rest_framework import permissions


class IsUserSelf(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        print(request, obj)
        return request.user == obj