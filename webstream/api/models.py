from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class User(User):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    followers = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=False, null=True)
    following = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=False, null=True)
    bio = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.username}"


class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=True)

    def __str__(self):
        return f"{self.name}"


class Topic(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)

    def __str__(self):
        return f"{self.name}"



class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)
    name = models.CharField(max_length=100, blank=False, null=True)
    likes = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=False, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True) 
    views = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=False, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} : {self.created}"



class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000, blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.body}"   












