from rest_framework.serializers import ModelSerializer, SlugRelatedField
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import MyUser, WatchList, Video, Comment, Topic

# class UserSerializer(ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('username',
#                  'password',
#                  'first_name',
#                  'last_name',
#                  'profile_image',
#                  'followers',
#                  'following',
#                  'bio')

#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'], validated_data['password'])
#         user.save()
#         return user

class MyUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=MyUser.objects.all())],
            min_length=5,
            max_length=20
            ),
    password = serializers.CharField(
            required=True,
            max_length=256
            )

    class Meta:
        model = MyUser
        fields = ('username', 'password')

    def create(self, validated_data):
        user = MyUser.objects.create_user(validated_data['username'], validated_data['password'])
        user.save()
        return user



class WatchListSerializer(ModelSerializer):

    user = SlugRelatedField(
        slug_field='username',
        queryset=MyUser.objects.all()
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
