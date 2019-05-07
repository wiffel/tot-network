from rest_framework.routers import DefaultRouter

from totaliatarian_network.users.views import UserCreateViewSet, UserViewSet

users_router = DefaultRouter()
users_router.register(r'users', UserCreateViewSet)
users_router.register(r'users', UserViewSet)
