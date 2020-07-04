from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',default='')
    profile_pic=models.ImageField(upload_to='profile_pic',default='1.jpg')

    def __str__(self):
        return self.user.username