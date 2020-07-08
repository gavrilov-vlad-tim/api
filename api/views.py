from rest_framework.filters import SearchFilter
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from django.shortcuts import get_object_or_404

from .models import Comment, Follow, Group, Post, User
from .permissions import IsOwnerPermission
from .serializers import (
    CommentSerializer, FollowSerializer,
    GroupSerializer, PostSerializer
)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsOwnerPermission 
    )

    filterset_fields = ('group', ) 

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsOwnerPermission
    )

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(CreateModelMixin, ListModelMixin, 
    GenericViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly, 
        IsOwnerPermission,
    )
    filter_backends = (SearchFilter, )
    search_fields = ['=user__username', '=following__username']

    def perform_create(self, serializer):
        following = get_object_or_404(User, 
        username=self.request.data.get('following'))
        serializer.save(user=self.request.user, following=following)


class GroupViewSet(CreateModelMixin, ListModelMixin,
    GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
