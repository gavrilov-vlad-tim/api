from rest_framework import serializers

from .models import Comment, Follow, Group, Post, User

from django.shortcuts import get_object_or_404


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        exclude = ('group', )
        model = Post
        read_only_fields = ('pub_date', )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
        read_only_fields = ('created', 'post')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    following = serializers.CharField(source='following.username')

    class Meta:
        fields = ('user', 'following')
        model = Follow
    
    def validate(self, data):
        following = get_object_or_404(User, username=data.get('following').get('username'))
        if Follow.objects.filter(user=self.context.get('request').user, 
            following=following).exists():
            raise serializers.ValidationError(detail='Bad request')
        return data


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title')
        model = Group        
