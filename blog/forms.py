from django import forms
from django.contrib.auth.models import User
from .models import Article, Comment, UserProfile


class ArticleForm(forms.ModelForm):
    """Form for the image model"""
    article_content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Article
        fields = ("headline", "article_content","article_photos","yt_links","article_image_upload","tag")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment_content",)

class UserForm(forms.ModelForm):
    email = forms.EmailField(required=True,label="Updated email address if different",
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ("email",)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("about_user","user_photo",)