from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

from django.urls import path, include

from .views import (
    CommentViewSet, FollowViewSet, 
    GroupViewSet, PostViewSet
)

v1_router =  DefaultRouter()
v1_router.register('posts', PostViewSet)
v1_router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
v1_router.register('follow', FollowViewSet)
v1_router.register('group', GroupViewSet)

urlpatterns = [
    path('', include(v1_router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
