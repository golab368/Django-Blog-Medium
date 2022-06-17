from django.contrib.auth.models import AbstractUser
from django.db import models
from taggit.managers import TaggableManager
from django.forms import IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    about_user = models.CharField(blank=True, max_length=255)
    user_photo = models.URLField(blank=True, max_length=300)

    def serialize(self):
        return {
            "id": self.id,
            "profile": self.profile,
            "about_user": self.about_user,
            "user_photo": self.user_photo,
        }


class Article(models.Model):
    headline = models.CharField(max_length=100)
    article_content = models.CharField(max_length=10000)
    article_author = models.ForeignKey(User, on_delete=models.CASCADE)
    article_links = models.URLField(blank=True, max_length=300)
    article_image_upload = models.ImageField(blank=True, upload_to="images/")
    slug = models.SlugField(null=True, unique=True, max_length=100)
    tag = TaggableManager(blank=True)
    likes = models.ManyToManyField(User, related_name="article_likes")
    timestamp = models.DateTimeField(auto_now_add=True)

    def serialize(self):

        return {
            "id": self.id,
            "headline": self.headline,
            "article_content": self.article_content,
            "article_author": self.article_author,
            "article_links": self.article_links,
            "article_image_upload": self.article_image_upload,
            "tag": self.tag,
            "likes": self.likes,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),

        }


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comment")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comment")
    comment_content = models.CharField(max_length=250)

    def serialize(self):

        return {
            "id": self.id,
            "article": self.article,
            "user": self.user,
            "comment_content": self.comment_content,

        }


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follow_writter_id = models.IntegerField()

    def serialize(self):

        return {
            "id": self.id,
            "user": self.user,
            "follow_writter_id ": self.follow_writter_id,
        }
