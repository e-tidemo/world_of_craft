from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Profile
#from crafts_posts.models import Post
from .serializers import ProfileSerializer
from drf_api.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404


class ProfileList(generics.ListAPIView):
    """
    List all profiles
    No Create view (post method), as profile creation handled by django signals
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        follower_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
    ]
    ordering_fields = [
        'posts_count',
        'follower_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
        'posts',
    ]
    
class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.prefetch_related('owner__post_set').annotate(
        posts_count=Count('owner__post', distinct=True),
        follower_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]
    """
    def get_object(self):
        # Get the profile object based on the provided username
        username = self.kwargs.get('username')
        profile = get_object_or_404(Profile, owner__username=username)
        
        # Fetch related posts
        profile.posts = profile.owner.post_set.all() 
        
        return profile

    """
