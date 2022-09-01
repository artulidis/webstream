from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        user = self.model(
            username=username
        )
        user.is_staff=True
        user.is_active=True
        user.is_superuser=True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)    

class MyUser(AbstractBaseUser):
    objects = MyUserManager()
    class Meta:
        # managed = False
        db_table = 'user_entity'

    id = models.AutoField(primary_key=True, db_column='userId')
    username = models.CharField(db_column='username', unique=True, max_length=20)
    password = models.CharField(db_column='userPassword', max_length=256)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.id) + " (%s)" % str(self.username)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True



class WatchList(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=True)

    def __str__(self):
        return f"{self.name}"


class Topic(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)

    def __str__(self):
        return f"{self.name}"



class Video(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True,)
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












