from django.test import TestCase
from blog.models import User, Article, Comment, Follow
from blog.forms import ArticleForm, CommentForm, UserForm, UserProfileForm


class TestForm(TestCase):
    def test_article_form(self):
        user_mark = User(username='mark', password='mark@mark.com', email='mark123')
        self.user_mark = user_mark
        user_mark.save()
        article = Article.objects.create(
            headline="5 SEO Hacks that Helped me Gain 2M+ Impressions on Google",
            article_content="It may seem low for two years time but thats because I was kind of inconsistent. Sometimes I was publishing over 15 articles a month and sometimes, only four.",
            article_author= user_mark,
            article_links="https://miro.medium.com/max/700/0*_WDjgb86rXu3-Qjg",
            tag="it, google",
        )
        data = {"headline":article.headline , "article_content":article.article_content,"article_links":article.article_links,"article_image_upload":"","tag":article.tag}
        form = ArticleForm(data=data)
        print("dsadasdasdasdasdasdasda",form)
        self.assertTrue(form.is_valid())

