from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('users/', views.UserListCreateApiView.as_view(), name='users'),
    path('user/<str:username>', views.UserRetrieveUpdateDestroyAPIView.as_view(), name='user'),


    path('watchlists/', views.WatchListListCreateApiView.as_view(), name='watchlists'),
    path('topics/', views.TopicListCreateApiView.as_view(), name='topics'),
    path('videos/', views.VideoListCreateApiView.as_view(), name='videos'),
    path('comments/', views.CommentListCreateApiView.as_view(), name='comments'),

    path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]