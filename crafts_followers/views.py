from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from crafts_followers.models import Followers
from crafts_followers.serializers import FollowerSerializer

class FollowersList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly],
    serializer_class = FollowerSerializer,
    queryset = Followers.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FollowersDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly],
    serializer_class = FollowerSerializer, 
    queryset = Followers.objects.all()