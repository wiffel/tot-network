from rest_framework.routers import DefaultRouter

from totaliatarian_network.posts.views import PostViewSet

posts_router = DefaultRouter()
posts_router.register(r'posts', PostViewSet,  basename='post')
