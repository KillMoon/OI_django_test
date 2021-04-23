from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from impresses.models import Impress


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('homePage')
        self.add_url = reverse('add')
        self.test_user = User.objects.create_user(username='test1', password='12345')
        self.test_user1 = User.objects.create_user(username='test2', password='12345')
        # self.impress_test = Impress.objects.create(
        #     name="qweasd",
        #     info="sadfgh"
        # )

    def test_impress_list_GET(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'impresses/homePage.html')

    def test_impress_list_GET_auth(self):
        login = self.client.login(username='test1', password='12345')
        Impress.objects.create(
            name="qweasd",
            info="sadfgh",
            user=self.test_user
        )
        response = self.client.get(self.home_url)

        self.assertEqual(response.context['impresses'][0].info, 'sadfgh')

        Impress.objects.create(
            name="qweasd",
            info="sadfgh",
            user=self.test_user
        )

        self.assertEqual(len(response.context['impresses']), 2)

    def test_impress_list_POST(self):
        login = self.client.login(username='test1', password='12345')
        response = self.client.post(self.add_url, {
            'name': 'qweasd',
            'info': 'sadfgh'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Impress.objects.first().name, 'qweasd')
        self.assertEqual(Impress.objects.first().info, 'sadfgh')
        self.assertEqual(Impress.objects.first().user.username, 'test1')
