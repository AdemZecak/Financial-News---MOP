from django.test.testcases import TestCase
from financial_news.models import Article

class TestModels(TestCase):

    def setUp(self):
        self.article = Article.objects.create(
            title = 'Article',
            author = 'Hesse',
        )
