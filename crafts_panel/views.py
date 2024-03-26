from rest_framework import generics, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser
from .models import Panel
from .serializers import PanelSerializer

class PanelCreateView(generics.CreateAPIView):
    queryset = Panel.objects.all()
    serializer_class = PanelSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionDenied("You do not have permission to create a panel post.")
        serializer.save()