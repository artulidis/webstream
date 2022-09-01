from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import MyUserSerializer
from .models import MyUser

from .serializers import WatchListSerializer
from .models import WatchList

from .serializers import TopicSerializer
from .models import Topic

from .serializers import VideoSerializer
from .models import Video

from .serializers import CommentSerializer
from .models import Comment

class MyUserListCreateApiView(generics.ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = MyUserSerializer
    lookup_field = 'username'

    def get_queryset(self):
        self.username = get_object_or_404(MyUser, username=self.kwargs['username'])
        return MyUser.objects.filter(username=self.username)


class WatchListListCreateApiView(generics.ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class TopicListCreateApiView(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class VideoListCreateApiView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class CommentListCreateApiView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer