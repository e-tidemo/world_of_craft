from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from .models import Panel

class PanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panel
        fields = ['id', 'owner', 'created_at', 'updated_at', 'title', 'content', 'image', 'video_url']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        # Set the owner of the post to the current user making the request
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
