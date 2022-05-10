from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import datetime


class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_img = models.CharField(max_length=200)
    post_text = models.CharField(max_length=200)
    post_date = models.DateTimeField('Data do post')
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title + ' | ' + str(self.post_author)

    def foi_publicada_recentemente(self):
        return self.post_date >= timezone.now() - datetime.timedelta(days=1)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)

    def __str__(self):
        return self.comment_text
