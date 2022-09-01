from django.contrib import admin
from django import forms
from .models import MyUser, WatchList, Video, Comment, Topic
from django.contrib.auth.admin import UserAdmin

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ( 'username', 
                   'password',
                   'first_name',
                   'last_name',
                   'profile_image',
                   'followers',
                   'following',
                   'bio' )

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class MyUserAdmin(UserAdmin):

    add_form = UserCreationForm
    list_display = ("username",)
    ordering = ("username",)
    list_filter = ("username", )

    fieldsets = (
        (None, {'fields': ( 'username',
                            'password',
                            'first_name',
                            'last_name',
                            'profile_image',
                            'followers',
                            'following',
                            'bio')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'username',
                        'password',
                        'first_name',
                        'last_name',
                        'profile_image',
                        'followers',
                        'following',
                        'bio' )}
            ),
        )

    filter_horizontal = ()

admin.site.register(MyUser, MyUserAdmin)
admin.site.register(WatchList)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Topic)
