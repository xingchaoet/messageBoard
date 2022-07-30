from django.db import models

class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    passwd = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

#用户踩赞
class UserBoardPost(models.Model):
    userid =  models.IntegerField(max_length=11, unique=True)
    boardpostid =  models.IntegerField(max_length=11, unique=True)
    good = models.IntegerField(default=0)
    bad = models.IntegerField(default=0)