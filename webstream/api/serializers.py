from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .models import User, WatchList, Video, Comment, Topic
from django.contrib.auth.hashers import make_password

class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'profile_image',
            'followers',
            'following',
            'bio'
        ]


class WatchListSerializer(ModelSerializer):

    user = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = WatchList
        fields = '__all__'


class TopicSerializer(ModelSerializer):

    class Meta:
        model = Topic
        fields = '__all__'


class VideoSerializer(ModelSerializer):

    topic = SlugRelatedField(slug_field='name', queryset=Topic.objects.all())

    watchlists = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = '__all__'


    
class CommentSerializer(ModelSerializer):

    video = SlugRelatedField(slug_field='name', queryset=Video.objects.all())

    class Meta:
        model = Comment
        fields = '__all__'
