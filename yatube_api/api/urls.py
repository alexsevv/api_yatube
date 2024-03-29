from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import PostsViewsSet, GroupsViewSet, CommentsViewSet

v1_router = routers.DefaultRouter()
v1_router.register(r'posts', PostsViewsSet, basename='posts')
v1_router.register(r'groups', GroupsViewSet, basename='groups')
v1_router.register(r'posts/(?P<post_id>\d+)/comments', CommentsViewSet,
                   basename='comments')


urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token, name='get_token'),
    path('v1/', include(v1_router.urls)),
]
