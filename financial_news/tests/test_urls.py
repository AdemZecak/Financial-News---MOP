from django.test import SimpleTestCase
from django.urls import reverse,resolve
from financial_news.views import article_list,article_detail


class TestUrls(SimpleTestCase):

    def test_article_list(self):
        url = reverse('article_list')
        print(resolve(url))
        self.assertEquals(resolve(url).func,article_list)


    def test_article_list(self):
        url = reverse('article_detail',args=['2'])
        print(resolve(url))
        self.assertEquals(resolve(url).func,article_detail)

