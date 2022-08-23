from rest_framework import mixins, viewsets
from rest_framework import permissions

from .permissions import IsUserSelf
from .serializers import (UserDetailCreateSerializer, 
                            UserUpdateSerializer)
from .renderers import UserRenderer
from .filters import SelfOrAllUsersFilter
from .models import User

from e_commerce.core.mixins import RedisCacheMixin


class UserListCreateView(RedisCacheMixin,
                          mixins.CreateModelMixin, 
                            mixins.ListModelMixin,
                                viewsets.GenericViewSet):
    serializer_class = UserDetailCreateSerializer
    queryset = User.objects.all()
    filter_backends = [SelfOrAllUsersFilter]
    
    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.IsAuthenticated()]
        return []


class UserDetailUpdateDeleteView(RedisCacheMixin,
                                  mixins.RetrieveModelMixin,
                                    mixins.UpdateModelMixin,
                                     mixins.DestroyModelMixin,
                                        viewsets.GenericViewSet):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()
    lookup_field = "slug"
    permission_classes = [IsUserSelf]
    renderer_classes = [UserRenderer]
