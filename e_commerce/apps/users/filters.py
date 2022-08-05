from rest_framework import filters


class SelfOrAllUsersFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if not request.user.is_superuser:
            return queryset.get(id=request.user.id)

        return queryset
