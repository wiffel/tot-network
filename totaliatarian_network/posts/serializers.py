from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = user = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault(),
        read_only=True)

    class Meta:
        model = Post
        fields = ('text', 'user')
