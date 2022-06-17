from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from blog.models import User, Article
from blog.views import *



class TestView(TestCase):
    
    def setUp(self):
        self.client = Client()
        user_mark = User(username='mark', password='mark@mark.com', email='mark123')
        user_mark.save()
        #self.logged_in = self.client.login(username='mark', password='mark123')

        #self.tag = reverse('tagged', args=['google',])
        #self.like = reverse('like', args=[0,])
        self.article_detail = reverse('article_detail', args=["7"])

        number_of_articles = 20
        for article_num in range(number_of_articles):
            article = Article.objects.create(
            headline=f"{article_num} SEO Hacks that Helped me Gain 2M+ Impressions on Google",
            article_content="It may seem low for two years time but thats because I was kind of inconsistent. Sometimes I was publishing over 15 articles a month and sometimes, only four.",
            article_author= user_mark,
            article_links="https://miro.medium.com/max/700/0*_WDjgb86rXu3-Qjg",
            tag="it, google",)
            article.save()
           #self.article = article
        print("dasdasdasdasdasdasdasda",self.client.login(username='fred', password='secret'))
        
    def test_home_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'web/home.html')

    def test_home_correct_resp(self):
        resp = reverse('home')
        self.assertEqual(resolve(resp).func, home)

    def test_article_url_correct_status_code(self): 
        resp = self.client.get('') 
        self.assertEqual(resp.status_code, 200)  
    

    def test_create_article_correct_resp(self):
        resp = reverse('create_article')
        self.assertEqual(resolve(resp).func, create_article)

    def test_article_detail_get(self):
        resp = reverse('article_detail', args=("7"))
        response = self.client.get(self.article_detail)
        self.assertEqual(resolve(resp).func, article_detail)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "web/article_detail.html")



"""    def test_something_view(self):
        self.client.force_login(self.logged_in)
        response = self.client.post(reverse('login_view'), follow=True)
        self.assertEqual(response.status_code, 200)"""