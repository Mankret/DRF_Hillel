from django.contrib.auth.models import User
from rest_framework import serializers
from drf_project.models import Post, Comment


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'posts', 'comments']


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comment_set = serializers.HyperlinkedRelatedField(many=True,  view_name='comment-detail', read_only=True)

    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'body', 'created', 'comment_set', 'owner']


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post = serializers.HyperlinkedRelatedField(many=False, source='post.id', view_name='post-detail', read_only=True)
    post_name = serializers.PrimaryKeyRelatedField(source='post', queryset=Post.objects.all(), write_only=True)

    class Meta:
        model = Comment
        fields = ['url', 'id', 'title', 'text', 'created', 'owner', 'post', 'post_name']
