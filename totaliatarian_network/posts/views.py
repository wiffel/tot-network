from rest_framework.viewsets import ModelViewSet

from totaliatarian_network.posts.models import Post
from totaliatarian_network.posts.permissions import IsOwnerOrReadOnly
from totaliatarian_network.posts.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    """
    Allows to list/get/create/update/delete Posts

    Note:
        - Only owner of a model can perform edit operations.
        - Private posts(Post.private field equals True) can be read only by 
        authenticated users
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        # if the user is authenticated return all including private
        if self.request.user.is_authenticated:
            return Post.objects.all()
        return Post.objects.filter(private=False)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
