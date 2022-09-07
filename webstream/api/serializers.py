from rest_framework.serializers import ModelSerializer, SlugRelatedField
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import MyUser, WatchList, Video, Comment, Topic


class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('username',
                  'password',
                  'email',
                  'full_name',
                  'profile_image',
                  'followers',
                  'following',
                  'bio')

    def create(self, validated_data):
        user = MyUser.objects.create_user(validated_data['username'], validated_data['password'])
        user.email = validated_data['email']
        user.full_name = validated_data['full_name']
        user.profile_image = validated_data['profile_image']
        user.followers = validated_data['followers']
        user.following = validated_data['following']
        user.bio = validated_data['bio']
        user.save()
        return user

    def update(self, user, validated_data):
        if validated_data['password'] is not None:
            user.set_password(validated_data['password'])
        user.username = validated_data['username']
        user.email = validated_data['email']
        user.full_name = validated_data['full_name']
        if validated_data['profile_image'] is not None:
            user.profile_image = validated_data['profile_image']
        else:
            user.profile_image = user.profile_image


        user.followers = validated_data['followers']
        user.following = validated_data['following']
        user.bio = validated_data['bio']
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

    topics = TopicSerializer(read_only=True, many=True)
    user = SlugRelatedField(slug_field='username', queryset=MyUser.objects.all())

    class Meta:
        model = Video
        fields = '__all__'


    
class CommentSerializer(ModelSerializer):

    video = SlugRelatedField(slug_field='name', queryset=Video.objects.all())

    class Meta:
        model = Comment
        fields = '__all__'
