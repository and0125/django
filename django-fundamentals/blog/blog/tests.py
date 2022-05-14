from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post 

class BlogTests(TestCase):

    @classmethod 
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser', email='test@email.com', password='secret'
        )
        cls.post = Post.objects.create(
            title = 'a good title',
            body = 'Nice body oddy',
            author = cls.user,
        )

    def test_post_contect(self):
        self.assertEqual(f"{self.post.title}", "a good title")
        self.assertEqual(f"{self.post.author}", 'testuser')
        self.assertEqual(f"{self.post.body}", "Nice body oddy")

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nice body oddy")
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'a good title')
        self.assertTemplateUsed(response, 'post_detail.html')