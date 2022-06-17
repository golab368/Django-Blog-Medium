from django.test import TestCase

# Create your tests here.
from blog.models import User, Article, Comment, Follow

import datetime

class TestUser(TestCase):

    def setUp(self):
        user_admin = User(username='admin',password='admin', email='admin@admin.com')
        user_admin.is_superuser = True
        user_admin.save()
        self.user_admin = user_admin

        user_mark = User(username='mark', password='mark@mark.com', email='mark123')
        user_mark.save()
        self.user_mark = user_mark

    def test_user_count(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2)

    def test_users_status(self):
        self.assertEquals(self.user_admin.is_superuser,True)
        self.assertEquals(self.user_mark.is_superuser,False)

class TestArticle(TestCase):

    def setUp(self):
        user_admin = User(username='admin',password='admin', email='admin@admin.com')
        user_admin.is_superuser = True
        user_admin.save()
        self.user_admin = user_admin

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
        self.article = article
        self.article.likes.set([user_admin.id, user_mark.id ])

    def test_headline_max_length(self):
        author=Article.objects.get(id=1)
        max_length = author._meta.get_field('headline').max_length
        self.assertEquals(max_length,100)

    def test_created_article_by_user(self):
        self.assertEquals(self.article.headline, "5 SEO Hacks that Helped me Gain 2M+ Impressions on Google")
        self.assertEquals(self.article.article_content, "It may seem low for two years time but thats because I was kind of inconsistent. Sometimes I was publishing over 15 articles a month and sometimes, only four.")
        self.assertEquals(self.article.article_author, self.user_mark)
        self.assertEquals(self.article.article_links, "https://miro.medium.com/max/700/0*_WDjgb86rXu3-Qjg")
        self.assertEquals(self.article.tag, "it, google")

    def test_article_likes(self):
        self.assertEquals(self.article.likes.count(), 2)

    def test_article_links(self):
        article=Article.objects.get(id=1)
        expected_link = article.article_links
        self.assertEquals(expected_link,self.article.article_links)

    def test_date(self):
        blog=Article.objects.get(id=1)
        the_date = blog.timestamp
        self.assertEquals(the_date.date(),datetime.date.today())

    def test_give_a_like(self):
        res = self.client.get(self.tag)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'tag/google/')

class TestComment(TestCase):

    def setUp(self):

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
        self.article = article
        
        comment = Comment.objects.create(
            article= article,
            user= user_mark,
            comment_content="Super!!!",
        )

        self.comment = comment

    def test_comment_user_id(self):
        comment=Comment.objects.get(id=1)
        expected_comment_user_id = comment.user
        self.assertEquals(expected_comment_user_id,self.comment.user)

    def test_comment_content_max_length(self):
        comment=Comment.objects.get(id=1)
        max_length = comment._meta.get_field('comment_content').max_length
        self.assertEquals(max_length,250)


class TestFollow(TestCase):

    def setUp(self):
        user_admin = User(username='admin',password='admin', email='admin@admin.com')
        user_admin.is_superuser = True
        user_admin.save()
        self.user_admin = user_admin

        user_mark = User(username='mark', password='mark@mark.com', email='mark123')
        user_mark.save()
        self.user_mark = user_mark

        follow = Follow.objects.create(user = user_admin, follow_writter_id = user_mark.id)
        self.follow = follow

    def test_user_name(self):
        follow=Follow.objects.get(id=1)
        expected_user_name = follow.user
        self.assertEquals(expected_user_name,self.follow.user)

    def test_follow_writter_id(self):
        follow=Follow.objects.get(id=1)
        expected_follow_writter_id= follow.follow_writter_id
        self.assertEquals(expected_follow_writter_id,self.follow.follow_writter_id)



